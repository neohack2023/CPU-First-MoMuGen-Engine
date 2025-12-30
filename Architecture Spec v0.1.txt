Technical Implementation of CPU-First Modular Music Generation Engines: Discrete Codecs, Optimized Transformers, and Deterministic Orchestration (v0.1)

Executive Summary

This document defines the technical architecture for a CPU-first, modular music generation engine. Unlike monolithic GPU-dependent models, this system utilizes a layered, iterative approach where instruments are generated as independent discrete token streams. The focus is on Real-Time Factor (RTF) targets, memory bandwidth optimization, and tiered cross-platform determinism.

1. Engine Default Configuration (v0.1)

The following defaults are locked to ensure immediate engineering focus and minimize train-inference mismatch:

|

| Component | Default Selection | Engineering Target / Justification |
| Neural Codec | EnCodec-style (24kHz, 6 kbps target, RVQ) | Target RTF < 1.0 on modern quad-core mobile/desktop. |
| Quantization | Static INT8 (Weights) | 4x footprint reduction; activations remain FP32/BF16. |
| Attention | GQA-8 (Grouped-Query) | Reduces KV-cache memory pressure; target speedup >1.2x. |
| Conditioning | Unified Metadata + Bar Indices | Shared cross-layer alignment format to prevent drift. |
| State Format | Atomic JSON + SHA256 | Ensures project integrity and cache-reuse. |

(Note: Exact model variant pinned at implementation time.)

2. Neural Audio Discretization: The RTF Boundary

The real-time factor (RTF) of the decoding stage is the primary constraint for the generation pipeline.

Codec Selection Criteria

Interactive Generation (RTF ≤ 1.0): Lightweight EnCodec-style architectures or PhiNet-derived codecs are required.

Optional High-Fidelity Path: DAC-class models (Descript Audio Codec) are reserved for offline rendering or high-fidelity stem upscaling where latency is secondary.

Optimization Strategy

PhiNet-Redesign: Evaluate inverted residual blocks to reduce encoder/decoder memory footprint.

RVQ Optimization: Investigate codebook dimensionality tradeoffs (e.g., 256 vs 1024 entries) for memory overhead reduction.

3. Timebase and Alignment

To ensure rhythmic coherence across independently generated layers, the engine enforces a unified timebase:

Musical Subdivisions: The engine operates on a grid of $PPQ$ (Pulses Per Quarter-note).

Default PPQ (v0.1): 96 pulses per quarter-note (subject to tuning).

Codec Frame Alignment: Codec frames (e.g., 20ms) are mapped to musical time based on the project BPM.

Alignment Strategy: Rhythm maps and bar indices are sampled at the codec frame rate. To avoid alignment drift, every generation run must snap to the nearest bar-start codec frame.

4. Optimized Transformer Architectures

The engine uses small autoregressive transformers (50M–150M parameters) per instrument.

Per-Instrument Model Spec (Targets)

| Layer | d_model | Heads | Context (Bars) | Justification |
| Drums | 512 | 8 | 16 | Rhythmic locality and loop variation. |
| Bass | 512 | 8 | 16 | Groove coherence with percussive layer. |
| Harmony | 768 | 12 | 32 | Long-range chord progression stability. |
| Lead | 512 | 8 | 8 | Phrase-based melodic "calls." |

Quantization Policy

Weights: Static INT8 quantization is mandatory for v0.1.

Activations: Remain in FP32 or BF16 to maintain dynamic range during intermediate calculations.

KV-Cache: 8-bit cache quantization is considered an optional, implementation-dependent optimization for long-context harmony layers.

Speculative Execution (Future Work)

Speculative execution (SpecExec) using a draft/verifier pattern is marked as a post-v0.1 enhancement to improve Time to First Token (TTFT).

5. Conditioning and Train-Inference Symmetry

To avoid "exposure bias" and distribution shift, the conditioning strategy must be identical during training and inference:

Strategy: Condition all models on a "Unified Global State" (BPM, Key, Section, and high-level Rhythm Map).

Implementation: Use a shared metadata embedding layer that consumes the same JSON-structured project state used by the CLI.

6. Deterministic Engineering: The "Git for Sound" Protocol

Reproducibility is essential for versioned music projects. v0.1 adopts a tiered guarantee model:

Tier 1 (Same Machine): Bit-exact waveform equality through fixed seeds and single-threaded execution.

Tier 2 (Same Architecture): Near-exact similarity; functional musical equivalence.

Tier 3 (Cross-Architecture): Functional equivalence. If waveform equality cannot be guaranteed (e.g., ARM vs x86), the Discrete Tokens serve as the canonical, immutable output of the generation run.

Hardware Execution Guards

import torch, os

def set_execution_guards():
    # Force consistent kernel implementation
    os.environ["ATEN_CPU_CAPABILITY"] = "avx2" 
    torch.set_num_threads(1)
    torch.set_num_interop_threads(1)
    torch.use_deterministic_algorithms(True)



Note: ATEN_CPU_CAPABILITY applies to x86 targets only. ARM builds rely on deterministic operator selection and single-threaded execution without ISA forcing.

7. Dataset Engineering and Metrics

Dataset preparation is decoupled from the runtime engine.

Dataset Stem Separation (Offline)

SCNet / HT-Demucs: Utilized solely for corpus preparation to extract clean training stems.

Quality Control: All training data must be pre-aligned to a global click track to ensure consistent tokenization.

Performance & Quality Metrics (Calibration Targets)

The following metrics are proposed for v0.1 calibration:

CBS (Cross-track Beat Synchrony): Initial Target ≥ 0.95.

IRS (Inner-track Rhythm Stability): Initial Target ≤ 0.02.

CBD (Cross-track Beat Dispersion): Initial Target ≤ 10ms.

8. v0.1 Acceptance Tests

Determinism Test: Ensure three sequential runs with the same seed yield identical token files.

Resumability Test: Verify a project can be stopped after "Run 1" and resumed for "Run 2" without state corruption.

Isolation Test: Regenerating the "Lead" layer must not alter the SHA256 hash of the "Drums" layer.

Performance Log: Every run must log RTF and peak memory usage to a system_telemetry.log.

9. Non-Goals (v0.1)

End-to-end vocal synthesis: Lyrics remain text-only; timing maps remain symbolic.

GPU acceleration: The engine is strictly optimized for CPU-only inference.

Real-time interactive UI: Focus is on CLI and headless engine functionality.

Speculative decoding optimizations: Reserved for post-v0.1 latency tuning.

Cross-machine waveform bit-identity: Tokens are the source of truth across differing architectures.
