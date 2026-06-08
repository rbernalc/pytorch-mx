"""
Live demo script — full benchmark across matrix sizes.
Paste into Colab (GPU runtime) or run locally with an available accelerator.
Ask the audience to predict the numbers before running.
"""
import torch
import time


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


def main() -> None:
    cpu = torch.device("cpu")
    acc = torch.accelerator.current_accelerator()

    print(f"PyTorch    : {torch.__version__}")
    print(f"Accelerator: {acc}")
    print()
    print(f"{'N':>6} | {'CPU (ms)':>10} | {'ACC (ms)':>10} | {'Speedup':>8}")
    print("-" * 45)

    for N in [10, 100, 500, 1000, 5000, 10000]:
        tc = benchmark(N, cpu)
        ta = benchmark(N, acc)
        flag = "  ← ACC slower!" if tc > ta * 0.9 and tc < ta else ""
        print(f"{N:6d} | {tc:10.3f} | {ta:10.3f} | {tc/ta:8.1f}x{flag}")


if __name__ == "__main__":
    main()
