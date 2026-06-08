"""
Q5 — When do you NOT see a benefit?
Demonstrates three failure modes: small tensors, transfer-dominated ops,
and sync overhead in sequential loops.
Requires PyTorch 2.x and an available accelerator.
"""
import torch
import time


# ── Shared benchmark helper ──────────────────────────────────────────────────

def benchmark(N: int, device: torch.device, warmup: int = 3, runs: int = 20) -> float:
    A = torch.randn(N, N, device=device)
    B = torch.randn(N, N, device=device)
    for _ in range(warmup):
        torch.mm(A, B)
    torch.accelerator.synchronize()
    t0 = time.perf_counter()
    for _ in range(runs):
        torch.mm(A, B)
    torch.accelerator.synchronize()
    return (time.perf_counter() - t0) / runs * 1000


# ── Situation 1: Small tensors ───────────────────────────────────────────────

def demo_small_tensors(cpu: torch.device, acc: torch.device) -> None:
    print("=== Situation 1: Small Tensors ===")
    print(f"{'N':>5}  {'CPU (ms)':>10}  {'ACC (ms)':>10}  {'Winner':>12}")
    print("-" * 45)
    for N in [10, 50, 100, 200, 500]:
        t_cpu = benchmark(N, cpu)
        t_acc = benchmark(N, acc)
        winner = "Accelerator" if t_acc < t_cpu else "CPU"
        print(f"{N:5d}  {t_cpu:10.3f}  {t_acc:10.3f}  {winner:>12}")
    print()


# ── Situation 2: Transfer overhead dominates ─────────────────────────────────

def end_to_end_cpu(N: int) -> float:
    A = torch.randn(N, N)
    B = torch.randn(N, N)
    t0 = time.perf_counter()
    _ = torch.mm(A, B)
    return (time.perf_counter() - t0) * 1000


def end_to_end_acc(N: int, device: torch.device) -> float:
    A = torch.randn(N, N)  # on CPU
    B = torch.randn(N, N)
    torch.accelerator.synchronize()
    t0 = time.perf_counter()
    # transfer + compute + transfer back
    _ = torch.mm(A.to(device), B.to(device)).cpu()
    torch.accelerator.synchronize()
    return (time.perf_counter() - t0) * 1000


def demo_transfer_dominates(acc: torch.device) -> None:
    print("=== Situation 2: Transfer Overhead Dominates (end-to-end) ===")
    print(f"{'N':>6}  {'CPU (ms)':>10}  {'ACC e2e (ms)':>13}  {'Winner':>12}")
    print("-" * 50)
    for N in [500, 1000, 5000]:
        tc = end_to_end_cpu(N)
        ta = end_to_end_acc(N, acc)
        winner = "CPU" if tc < ta else "Accelerator"
        print(f"{N:6d}  {tc:10.1f}  {ta:13.1f}  {winner:>12}")
    print()


# ── Situation 3: Sync overhead in sequential loops ───────────────────────────

def demo_sync_in_loop(acc: torch.device, steps: int = 50) -> None:
    print("=== Situation 3: Sync Overhead in Sequential Loop ===")
    N = 500
    x = torch.randn(N, N, device=acc)
    W = torch.randn(N, N, device=acc)
    threshold = 1e6

    # BAD: .item() forces sync every iteration
    x_bad = x.clone()
    torch.accelerator.synchronize()
    t0 = time.perf_counter()
    for step in range(steps):
        x_bad = torch.mm(x_bad, W)
        if x_bad.max().item() > threshold:  # sync on every step!
            break
    torch.accelerator.synchronize()
    t_bad = (time.perf_counter() - t0) * 1000

    # GOOD: sync only once at the end
    x_good = x.clone()
    torch.accelerator.synchronize()
    t0 = time.perf_counter()
    for step in range(steps):
        x_good = torch.mm(x_good, W)
    result = x_good.max().item()   # single sync at the end
    torch.accelerator.synchronize()
    t_good = (time.perf_counter() - t0) * 1000

    print(f"  BAD  (sync every step) : {t_bad:.1f} ms")
    print(f"  GOOD (sync once)       : {t_good:.1f} ms")
    print(f"  Overhead from syncs    : {t_bad - t_good:.1f} ms")
    print(f"  (final max value: {result:.2e})")
    print()


# ── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    print(f"PyTorch {torch.__version__}")
    acc = torch.accelerator.current_accelerator()
    print(f"Accelerator: {acc}\n")

    cpu = torch.device("cpu")
    demo_small_tensors(cpu, acc)
    demo_transfer_dominates(acc)
    demo_sync_in_loop(acc)


if __name__ == "__main__":
    main()
