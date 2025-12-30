"""Execution guards that enforce deterministic CPU behavior for v0.1.

The guard function mirrors the architecture spec guidance for single-threaded
and deterministic kernel selection.
"""

import os


def set_execution_guards() -> None:
    """Apply deterministic execution settings for CPU-first runs."""

    import torch

    os.environ["ATEN_CPU_CAPABILITY"] = "avx2"
    torch.set_num_threads(1)
    torch.set_num_interop_threads(1)
    torch.use_deterministic_algorithms(True)
