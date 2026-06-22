# Daily Research Note - 2026-06-22

Status: candidate/working note for developer + LLM review. Do not treat as canon until reviewed.

## Repo context read
- README frames CPU-First-MoMuGen-Engine as a modular music generation engine that avoids monolithic GPU dependence.
- The stated architecture direction is layered, iterative generation where instruments are independent discrete token streams.
- Prior notes identify Real-Time Factor targets, memory bandwidth, deterministic fixtures, and token-stream latency as the first measurable frontier.

## Why this matters
The repo’s thesis lives or dies on benchmarks. Before model architecture grows teeth, the project needs a tiny timing harness that can tell fantasy from feasible CPU music generation.

## Useful findings with sources
- GitHub Actions secure-use guidance supports least-privilege CI and careful handling of generated artifacts. Source: https://docs.github.com/en/actions/reference/security/secure-use
- Transformers.js is useful as a browser-side model reference point if a lightweight demo lane is later added, but the engine core should keep CPU/runtime targets explicit. Source: https://huggingface.co/docs/transformers.js/en/index

## Candidate implementation ideas
1. Add `docs/BENCHMARK_PLAN.md` with device tiers, RTF target, memory target, instrument-token latency, and deterministic replay requirements.
2. Add a mock token-stream generator first, then measure generation time without needing a real model.
3. Add `TokenStreamReceipt`: seed, instrument lane, token count, wall time, RTF, memory estimate, and deterministic hash.
4. Add CI smoke tests for deterministic mock streams before adding real generation code.

## Risks / drift warnings
- Do not claim CPU real-time generation without timing logs.
- Do not couple instrument streams before stream independence is tested.
- Do not add GPU acceleration until CPU baseline numbers exist.

## Next dev / LLM actions
- Draft the benchmark plan.
- Implement a mock token-stream fixture.
- Add one CI check that verifies deterministic hash stability.
