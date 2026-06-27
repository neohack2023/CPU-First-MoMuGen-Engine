# Daily Research Note - 2026-06-27

Status: candidate/working note for developer + LLM review. Do not treat as canon until reviewed.

## Repo context read
- Prior passes identify this repo as a CPU-first music generation engine with deterministic token streams and benchmark receipts.
- Recent notes focused on CPU baseline testing before heavier model/runtime claims.

## Why this matters
CPU-first only means something if latency, determinism, and quality are measured on modest hardware with repeatable prompts/seeds.

## Useful findings with citations
- Transformers.js documents browser-side inference workflows that can inform optional lightweight model experiments: https://huggingface.co/docs/transformers.js/en/index
- GitHub Actions secure-use guidance recommends least-privilege workflow permissions and cautious artifact handling: https://docs.github.com/en/actions/reference/security/secure-use

## Candidate implementation ideas
1. Add `benchmark-receipt.json` with hardware_profile, seed, prompt_hash, model_or_algorithm, runtime_ms, output_hash, and pass_fail_notes.
2. Add a deterministic no-model baseline generator for comparison.
3. Add a fixture that checks the same seed emits the same token stream.
4. Add docs separating composition quality from runtime performance.

## Risks / drift warnings
- Do not compare model outputs without hardware profiles.
- Do not claim CPU feasibility from one machine.
- Keep model downloads out of default CI.

## Next suggested dev / LLM actions
- Draft benchmark receipt schema.
- Add deterministic baseline fixture.
- Add local-only benchmark instructions.
