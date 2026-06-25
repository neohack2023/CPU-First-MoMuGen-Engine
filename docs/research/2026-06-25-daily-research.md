# Daily Research Note - 2026-06-25

Status: candidate/working note for developer + LLM review. Do not treat as canon until reviewed.

## Repo context read
- Repo metadata describes CPU-First-MoMuGen-Engine as a modular music generation engine using independent discrete token streams, real-time factor targets, memory bandwidth optimization, and tiered CPU-first design.
- Prior notes focused on benchmark plans, deterministic token-stream receipts, and avoiding GPU-first assumptions.
- The broader repo system is adding local SLM workflows, so benchmarks should remain deterministic before advisory agents are introduced.

## Why this matters
The CPU-first claim needs repeatable proof: model size, token rate, latency, memory use, and quality proxy records that can run on modest hardware.

## Useful findings with citations
- GitHub secure-use guidance recommends least-privilege automation and careful handling of generated artifacts. Source: https://docs.github.com/en/actions/reference/security/secure-use
- Transformers.js documents browser-side model workflows and supported model families, useful as a comparison lane for CPU/browser experiments. Source: https://huggingface.co/docs/transformers.js/en/index
- Agentic workflow injection research is relevant if benchmark comments or issue text become agent instructions. Source: https://arxiv.org/abs/2605.07135

## Candidate implementation ideas
1. Add `benchmark_receipt.json`: CPU, RAM, OS, model, quantization, tokens/sec, RTF, memory peak, and pass/fail.
2. Add deterministic seed streams for drums, bass, melody, and arrangement.
3. Add a no-model baseline that proves the harness works before model tests.
4. Add a comparison matrix for local Python, browser JS, and future SLM advisor lanes.

## Risks / drift warnings
- Do not claim real-time performance without RTF receipts.
- Keep musical quality notes separate from speed metrics.
- Avoid GPU fallback creeping into CPU-first baseline tests.

## Next suggested dev / LLM actions
- Draft `docs/BENCHMARK_RECEIPTS.md`.
- Add one deterministic token-stream fixture.
- Add CI that validates benchmark receipt schema without requiring a large model.
