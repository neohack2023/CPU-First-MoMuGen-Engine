# Daily Research Note - 2026-06-23

Status: candidate/working note for developer + LLM review. Do not treat as canon until reviewed.

## Repo context read
- CPU-First-MoMuGen-Engine focuses on CPU-first music generation, benchmarks, deterministic streams, and practical low-resource constraints.
- Prior notes emphasize benchmark plans and token-stream receipts.

## Why this matters
CPU-first generation needs honest latency and repeatability numbers before the architecture grows into GPU-shaped wishful thinking.

## Useful findings with citations
- GitHub secure-use guidance recommends least-privilege workflows and careful generated-artifact handling. Source: https://docs.github.com/en/actions/reference/security/secure-use
- Transformers.js documents browser/JavaScript model workflows, useful as a comparison lane for local small-model experiments. Source: https://huggingface.co/docs/transformers.js/en/index

## Implementation ideas
1. Add benchmark receipts with CPU, RAM, OS, model, quantization, sample length, latency, and failure mode.
2. Add deterministic token-stream fixtures before quality claims.
3. Add a no-model baseline for rule-based generation.
4. Add an escalation rule for when a task needs a larger model or offline render.

## Risks / drift warnings
- Do not claim usable generation without benchmark receipts.
- Keep CPU-first constraints explicit; avoid hidden cloud/GPU assumptions.
- Separate evaluation metrics from taste notes.

## Next suggested dev / LLM actions
- Draft `docs/BENCHMARK_RECEIPTS.md`.
- Add first deterministic generation fixture.
- Add a local hardware baseline note for the user’s available CPU path.
