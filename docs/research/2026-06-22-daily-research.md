# Daily Research Note - 2026-06-22

Status: candidate/working note for developer + LLM review. Do not treat as canon until reviewed.

## Repo context read
- Prior notes identify CPU-First-MoMuGen-Engine as a modular music generation engine avoiding monolithic GPU dependence.
- The stated direction is layered iterative generation with independent instrument token streams.
- Current focus includes Real-Time Factor targets, memory bandwidth optimization, and tiered cross-platform determinism.

## Why this matters
This repo needs benchmark truth before architectural fireworks. The next useful target is a CPU-first performance ledger that makes every “real-time” claim measurable.

## Useful findings with citations
- GitHub Actions secure-use guidance recommends least-privilege automation and careful handling of generated artifacts. Source: https://docs.github.com/en/actions/reference/security/secure-use
- OpenSSF Scorecard maintenance research in 2026 treats repo activity and maintenance signals as measurable risk inputs. Source: https://arxiv.org/abs/2601.18344
- Vite is only relevant for a future browser demo shell; its current guide documents Node requirements and scaffold options. Source: https://vite.dev/guide/

## Candidate implementation ideas
1. Add `BenchmarkReceipt`: device tier, CPU, RAM, OS, model/mock stream, token count, latency, RTF, memory peak, pass/fail.
2. Add deterministic mock instrument streams before real generation.
3. Add per-instrument timing so independence is measured, not assumed.
4. Add a browser demo boundary doc: UI is optional, engine core remains CPU-first.

## Risks / drift warnings
- Do not claim real-time viability without timing logs.
- Do not couple streams before the independent stream contract is tested.
- Do not add GPU shortcuts before CPU baselines exist.

## Next dev / LLM actions
- Draft `docs/BENCHMARK_RECEIPTS.md`.
- Add mock token-stream timing tests.
- Define first low/mid/high CPU device tiers.
