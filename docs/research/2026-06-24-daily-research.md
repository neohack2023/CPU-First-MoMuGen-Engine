# Daily Research Note - 2026-06-24

Status: candidate/working note for developer + LLM review. Do not treat as canon until reviewed.

## Repo context read
- Repo context and recent PRs frame this project around CPU-first music/motif generation, benchmark plans, deterministic fixtures, and token-stream receipts.

## Why this matters
CPU-first generation needs boring, repeatable measurements before model or synthesis complexity increases.

## Useful findings
- GitHub Actions secure-use guidance recommends least-privilege workflows and careful secret/artifact handling: https://docs.github.com/en/actions/reference/security/secure-use
- Transformers.js provides a browser/local inference lane worth comparing later, but deterministic baselines should come first: https://huggingface.co/docs/transformers.js/en/index

## Candidate implementation ideas
1. Define `GenerationRunReceipt` with seed, prompt/spec, token stream hash, runtime, CPU budget, and output summary.
2. Add deterministic fixtures for short motif, repeated motif, and invalid request.
3. Track wall-clock runtime and memory for each fixture.
4. Keep any SLM scoring optional until deterministic checks exist.

## Risks / drift warnings
- Do not optimize for one machine without recording hardware.
- Do not add GPU assumptions to a CPU-first repo.
- Avoid claiming musical quality without a rubric.

## Next suggested dev / LLM actions
- Draft benchmark receipt schema.
- Add first deterministic token-stream fixture.
- Add hardware baseline fields to experiment logs.
