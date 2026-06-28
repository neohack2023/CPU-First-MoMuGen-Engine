# Daily Research Note - 2026-06-28

Status: candidate / working note for developer + LLM review. Do not treat as canon until reviewed.

## Repo context read
- README defines CPU-First-MoMuGen as a modular music generation engine using independent discrete token streams.
- The stated focus is Real-Time Factor targets, memory bandwidth optimization, and tiered cross-platform determinism.
- Recent open PR history focused on benchmark receipts and deterministic CPU-first baselines.

## Why this matters
The repo needs benchmark receipts before architecture grows. A CPU-first engine can only prove its lane if every generation experiment records timing, determinism, and memory pressure.

## Useful findings
- GitHub Actions secure-use guidance recommends least-privilege workflows and careful artifact handling. Source: https://docs.github.com/en/actions/reference/security/secure-use
- Transformers.js shows browser/JS model execution is possible, useful as a later comparison lane but not a CPU determinism substitute. Source: https://huggingface.co/docs/transformers.js/en/index
- MCP security research supports keeping tool/model routing auditable when agents are added. Source: https://arxiv.org/abs/2511.20920

## Implementation ideas
1. Add `BenchmarkReceipt`: CPU, OS, Python/Node version, model/layer, token stream count, seed, RTF, memory peak, and output checksum.
2. Add a deterministic baseline generator before any neural lane.
3. Add three benchmark tiers: tiny smoke, normal dev, and long-run endurance.
4. Record instrument streams separately so failures can be traced by lane.

## Risks / drift warnings
- Do not compare model quality without matching CPU/time budgets.
- Do not call generation deterministic unless seed + output checksum replay passes.
- Avoid GPU assumptions in docs or tests.

## Next dev / LLM actions
- Draft `docs/benchmark-receipt.md`.
- Add one deterministic token-stream smoke fixture.
- Add a benchmark table template for future experiments.
