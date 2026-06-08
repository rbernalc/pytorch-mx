"""
Q3 — Benchmark: speedup of torch.mm vs matrix size N.
Shows crossover point, roofline regime, and correct synchronization.
Requires PyTorch 2.x and an available accelerator.
"""
import torch
import time


def benchmark(N: int, device: torch.device, warmup: int = 3, runs: int = 20) -> float:
    """Return average time per torch.mm call in milliseconds."""
    A = torch.randn(N, N, device=device)
    B = torch.randn(N, N, device=device)
    for _ in range(warmup):
        torch.mm(A, B)
    torch.accelerator.synchronize()   # flush warm-up
    t0 = time.perf_counter()
    for _ in range(runs):
        torch.mm(A, B)
    torch.accelerator.synchronize()   # wait for all work to complete
    return (time.perf_counter() - t0) / runs * 1000


def main() -> None:
    print(f"PyTorch {torch.__version__}")
    acc = torch.accelerator.current_accelerator()
    print(f"Accelerator: {acc}\n")

    cpu = torch.device("cpu")

    print(f"{'N':>6} | {'CPU (ms)':>10} | {'ACC (ms)':>10} | {'Speedup':>8}")
    print("-" * 45)

    sizes = [10, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    for N in sizes:
        t_cpu = benchmark(N, cpu)
        t_acc = benchmark(N, acc)
        speedup = t_cpu / t_acc
        flag = "  ← ACC slower!" if speedup < 1.0 else ""
        print(f"{N:6d} | {t_cpu:10.3f} | {t_acc:10.3f} | {speedup:8.1f}x{flag}")


if __name__ == "__main__":
    main()
