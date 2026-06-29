# Daily Research Note - 2026-06-29

Status: candidate / working note. Review before promotion.

## Repo context read
- Prior repo context frames this project as a CPU-first music/motif generation engine with deterministic fixtures, benchmark plans, and token-stream receipts.
- Earlier research passes emphasized avoiding GPU assumptions and documenting reproducible generation paths.

## Why this matters
The repo’s edge is CPU-first repeatability. The highest-value research is a benchmark-and-receipt path that proves small generation steps are deterministic, measurable, and useful before model complexity grows.

## Useful findings
- Transformers.js documents browser-side and JavaScript inference paths that may be useful for lightweight local comparison later, but not as a replacement for CPU-first baselines: https://huggingface.co/docs/transformers.js/en/index
- GitHub Actions secure-use guidance supports least-privilege CI and careful handling of generated artifacts: https://docs.github.com/en/actions/reference/security/secure-use
- MCP governance research recommends provenance and scoped authorization for agent/tool workflows: https://arxiv.org/abs/2511.20920

## Candidate implementation ideas
1. Add a `GenerationReceipt`: seed, generator version, input constraints, token stream, timing, output hash, and warnings.
2. Define benchmark tiers: tiny smoke, normal local, and stress test.
3. Add one deterministic motif fixture that CI can run without large dependencies.
4. Compare deterministic baseline output against any future SLM/model-assisted path.

## Risks / drift warnings
- Do not require GPU or heavyweight model downloads for baseline validation.
- Do not claim musical quality from speed metrics alone.
- Avoid hidden randomness; every generated candidate should carry seed/version data.

## Next suggested dev / LLM actions
- Add the smallest deterministic generation fixture.
- Document expected runtime on a modest CPU.
- Keep model-assisted generation as a later adapter lane.