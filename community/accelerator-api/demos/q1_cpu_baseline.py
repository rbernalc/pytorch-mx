"""
Q1 — CPU baseline: time torch.mm for increasing matrix sizes.
No GPU required. Shows how CPU time scales with N.
"""
import torch
import time


def time_mm_cpu(N: int, runs: int = 10) -> float:
    A = torch.randn(N, N)
    B = torch.randn(N, N)
    # warmup
    for _ in range(3):
        torch.mm(A, B)
    t0 = time.perf_counter()
    for _ in range(runs):
        torch.mm(A, B)
    return (time.perf_counter() - t0) / runs * 1000  # ms


if __name__ == "__main__":
    print(f"PyTorch {torch.__version__}")
    print(f"{'N':>6}  {'ms':>10}")
    print("-" * 20)
    for N in [10, 100, 500, 1000, 5000]:
        ms = time_mm_cpu(N)
        print(f"{N:6d}  {ms:10.3f} ms")
