"""
Q4 — Hidden costs: data transfer, kernel launch overhead, first-run warm-up.
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


# ── Cost 1: Data transfer ────────────────────────────────────────────────────

def measure_transfer(N: int, device: torch.device) -> tuple[float, float, float]:
    A = torch.randn(N, N)  # on CPU
    size_mb = A.nbytes / 1e6
    torch.accelerator.synchronize()
    t0 = time.perf_counter()
    A_dev = A.to(device)   # host → accelerator memory
    torch.accelerator.synchronize()
    transfer_ms = (time.perf_counter() - t0) * 1000
    bandwidth_mb_s = size_mb / transfer_ms * 1000
    return size_mb, transfer_ms, bandwidth_mb_s


def demo_transfer(device: torch.device) -> None:
    print("=== Cost 1: Data Transfer ===")
    print(f"{'N':>6}  {'Size (MB)':>10}  {'Transfer (ms)':>14}  {'Compute (ms)':>13}")
    print("-" * 50)
    for N in [100, 500, 1000, 5000]:
        size_mb, t_ms, _ = measure_transfer(N, device)
        t_compute = benchmark(N, device)
        print(f"{N:6d}  {size_mb:10.2f}  {t_ms:14.2f}  {t_compute:13.3f}")
    print()


# ── Cost 2: Kernel launch overhead ──────────────────────────────────────────

def demo_kernel_launch(device: torch.device) -> None:
    print("=== Cost 2: Kernel Launch Overhead ===")
    A = torch.randn(10, 10, device=device)
    B = torch.randn(10, 10, device=device)

    torch.accelerator.synchronize()
    t0 = time.perf_counter()
    _ = torch.mm(A, B)
    torch.accelerator.synchronize()
    acc_ms = (time.perf_counter() - t0) * 1000

    A_cpu = torch.randn(10, 10)
    B_cpu = torch.randn(10, 10)
    t0 = time.perf_counter()
    _ = torch.mm(A_cpu, B_cpu)
    cpu_ms = (time.perf_counter() - t0) * 1000

    print(f"Kernel launch + 10x10 on accelerator : {acc_ms:.3f} ms")
    print(f"CPU 10x10 matmul                     : {cpu_ms:.3f} ms")
    print(f"Overhead ratio                        : {acc_ms/cpu_ms:.1f}x\n")


# ── Cost 3: First-run warm-up ────────────────────────────────────────────────

def demo_warmup(device: torch.device) -> None:
    print("=== Cost 3: First-Run Warm-Up ===")
    N = 1000
    A = torch.randn(N, N, device=device)
    B = torch.randn(N, N, device=device)
    for i in range(6):
        torch.accelerator.synchronize()
        t0 = time.perf_counter()
        _ = torch.mm(A, B)
        torch.accelerator.synchronize()
        ms = (time.perf_counter() - t0) * 1000
        label = "  ← context init + kernel plan selection" if i == 0 else ""
        print(f"  Run {i}: {ms:7.1f} ms{label}")
    print()


# ── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    print(f"PyTorch {torch.__version__}")
    device = torch.accelerator.current_accelerator()
    print(f"Accelerator: {device}\n")

    demo_transfer(device)
    demo_kernel_launch(device)
    demo_warmup(device)


if __name__ == "__main__":
    main()
