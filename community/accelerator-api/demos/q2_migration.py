"""
Q2 — Minimal migration: CPU vs accelerator with device-agnostic API.
Requires PyTorch 2.x and an available accelerator (GPU, MPS, etc.).
"""
import torch


def main() -> None:
    print(f"PyTorch {torch.__version__}")

    device = torch.accelerator.current_accelerator()
    print(f"Accelerator: {device}\n")

    N = 1000
    A = torch.randn(N, N)
    B = torch.randn(N, N)

    # ---- CPU ----
    C_cpu = torch.mm(A, B)
    print(f"CPU result device : {C_cpu.device}")

    # ---- Accelerator: move tensors with .to(device) ----
    C_acc = torch.mm(A.to(device), B.to(device))
    print(f"ACC result device : {C_acc.device}")

    # ---- Preferred: create directly on device ----
    A2 = torch.randn(N, N, device=device)
    B2 = torch.randn(N, N, device=device)
    C2 = torch.mm(A2, B2)
    print(f"ACC (no transfer) : {C2.device}")

    print("\nResults match:", torch.allclose(C_cpu, C_acc.cpu(), atol=1e-3))


if __name__ == "__main__":
    main()
