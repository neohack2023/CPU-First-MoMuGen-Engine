# Daily Research Note - 2026-06-26

Status: candidate / working note for developer and LLM review.

## Repo context read
- Repo direction centers on CPU-first procedural music generation, benchmark plans, deterministic fixtures, and token/event streams.
- Prior notes emphasized deterministic baselines and benchmark receipts.

## Why this matters
CPU-first generation needs proof that musical results are reproducible and cheap before adding bigger model layers. Today’s slice is a benchmark receipt tied to generated token streams.

## Useful findings
- GitHub Actions secure-use guidance recommends least-privilege CI and careful treatment of generated artifacts: https://docs.github.com/en/actions/reference/security/secure-use
- MCP security research warns that tool capability ambiguity can cause unsafe agent behavior, useful when designing local generation helpers: https://arxiv.org/abs/2601.17549

## Candidate implementation ideas
1. Add `GenerationBenchmarkReceipt`: seed, prompt fragment, token stream hash, CPU time, memory estimate, musical validity flags, and rejected reasons.
2. Add one deterministic melody/rhythm fixture that can be regenerated exactly.
3. Add docs separating deterministic engine outputs from LLM commentary.
4. Add CI that compares a known seed output hash.

## Risks / drift warnings
- Do not benchmark subjective quality before reproducibility exists.
- Avoid GPU/cloud assumptions.
- Do not let SLM commentary rewrite engine state.

## Next suggested dev / LLM actions
- Draft receipt schema.
- Add first seed/output hash fixture.
- Add README note explaining CPU-first proof standards.
