# Daily Research Note - 2026-06-21

Status: candidate/working note for developer + LLM review. Do not treat as canon until reviewed.

## Repo context read
- README describes CPU-First-MoMuGen-Engine as a modular music generation engine that avoids monolithic GPU dependence.
- The stated direction is layered, iterative generation where instruments are independent discrete token streams.
- Current stated focus: Real-Time Factor targets, memory bandwidth optimization, and tiered cross-platform determinism.

## Why this matters
The repo is thin but has a clear technical thesis. Research should define measurable CPU-first constraints before architecture grows around vibes instead of benchmarks.

## Current external findings
- GitHub Actions secure-use guidance recommends least-privilege workflow defaults and careful handling of generated/untrusted content. Source: https://docs.github.com/en/actions/reference/security/secure-use
- Vite’s Node baseline is useful only if a browser UI/prototype lane is added; the core engine should keep runtime targets explicit. Source: https://vite.dev/guide/

## Candidate implementation ideas
1. Add a research charter defining RTF targets by device tier: low-end desktop CPU, mid desktop CPU, mobile/laptop CPU.
2. Add a `docs/BENCHMARK_PLAN.md` with memory bandwidth, token-stream latency, and per-instrument generation timing.
3. Define deterministic seed fixtures: same prompt/seed/instrument stream should produce repeatable token output.
4. Separate engine core from any UI/demo shell early.

## Risks / drift warnings
- Do not claim CPU real-time viability without timing logs.
- Avoid coupling instrument streams before the independence contract is tested.
- Do not add GPU acceleration until CPU baseline numbers exist.

## Next dev / LLM actions
- Draft benchmark-plan and deterministic fixture docs.
- Define a minimal instrument-token schema.
- Add a first smoke test target that measures generation timing, even with mock token streams.
