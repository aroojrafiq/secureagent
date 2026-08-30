# Build Trajectory: Final Hard-Holdout Comparison

## 1. Metadata

- Date: 2026-08-30
- Documentation agent: GitHub Copilot in VS Code Agent mode
- Model policy: Copilot Student Auto model selection
- Underlying automatically selected model: unknown
- Evaluation operator: human evaluator
- Comparison report: `evaluation/HARD_HOLDOUT_COMPARISON.md`
- Protocol: `evaluation/HARD_HOLDOUT_PROTOCOL.md`

## 2. Goal

The goal was to produce the final evidence-backed comparison between the frozen generic one-pass baseline and the byte-identical SecureAgent-guided hard-holdout run without altering either result.

## 3. Evidence Inputs

- Protocol pre-registration commit: `f402e34`
- Frozen comparison-input commit: `8a1d029`
- Generic result commit: `ff7543a`
- SecureAgent-guided result commit: `be6920b`
- Source-harness validation: `traces/build/019-hard-holdout-harness-validation.md`
- Generic result: `evaluation/runs/baseline_official_03_hard_holdout/RESULT.md`
- Generic trajectory: `traces/build/020-generic-hard-holdout-baseline.md`
- Generic Bandit evidence: `evaluation/runs/baseline_official_03_hard_holdout/bandit-results.json`
- Guided result: `evaluation/runs/secureagent_official_01_hard_holdout/RESULT.md`
- Guided trajectory: `traces/build/021-secureagent-guided-hard-holdout.md`
- Guided pre-repair Bandit evidence: `evaluation/runs/secureagent_official_01_hard_holdout/bandit-before.json`
- Guided post-repair Bandit evidence: `evaluation/runs/secureagent_official_01_hard_holdout/bandit-after-01.json`

## 4. Fairness Controls

- Both repair runs began from byte-identical 18-file Python inputs.
- Neither run received a copied `ground_truth.json`.
- Source-to-run and cross-run hash mismatches were 0.
- Both used the same public tests, agent-blinded evaluator tests, success criteria, and Copilot Student Auto model-selection policy.
- Both prohibited test and package-file modifications.
- The evaluator-test source remained unavailable to both repair agents.
- The intentional intervention difference was workflow access.
- The generic baseline received one repair pass without scanner access or retries.
- The guided run received scanning, evaluator feedback, proposal review, bounded human approval, repair, and rescanning.
- The underlying automatically selected model was unknown and may not have been identical.

## 5. Frozen Results

| Metric | Generic baseline | SecureAgent-guided | Difference |
| --- | ---: | ---: | ---: |
| Fully resolved cases | 2 of 3 | 3 of 3 | +1 |
| Full case-resolution rate | 66.7% | 100% | +33.3 percentage points |
| Behaviorally repaired cases | 3 of 3 | 3 of 3 | 0 |
| Post-repair tests passed | 11 of 11 | 11 of 11 | 0 |
| Required findings remaining | 1 | 0 | -1 |
| New high-severity findings | 0 | 0 | 0 |
| Regression failures | 0 | 0 | 0 |
| Repair retries after valid verification | 0 | 0 | 0 |
| Unauthorized file modifications | 0 | 0 | 0 |

## 6. Per-Case Result

| Case | Generic baseline | SecureAgent-guided |
| --- | --- | --- |
| Case 11 | Resolved | Resolved |
| Case 12 | Resolved | Resolved |
| Case 13 | All tests passed, but B608 remained | All tests passed and B608 was removed |

## 7. Interpretation

- Both workflows repaired all tested runtime behavior.
- The behavioral test result was tied at 11 of 11.
- The generic baseline's allowlist retained formatted SQL and residual B608.
- The guided workflow's initial scan exposed B608 before repair.
- Human approval required literal SQL branches or fixed templates.
- The guided post-repair rescan confirmed zero findings.
- The measured improvement was therefore verification completeness and residual-target removal.
- The result does not imply that the generic agent failed to identify all three vulnerability classes.

## 8. Workflow Evidence

- The generic baseline produced a concise one-pass repair with zero retry overhead.
- The guided workflow produced before-and-after scanner artifacts, an explicit repair proposal, bounded human authorization, a reviewed diff, and post-repair rescan evidence.
- Three controlled guided-run command reruns were caused by invalid Copilot tool output.
- Those reruns were operational overhead, not repair retries, because the invalid attempts produced no usable result.
- No repair retry occurred after a valid verification result.
- Invalid tool attempts were documented rather than hidden.

## 9. Limitations Preserved

- Only three synthetic holdout cases were compared.
- Each workflow was run once.
- The underlying automatically selected model was unknown.
- Evaluator blinding depended on protocol restrictions rather than cryptographic isolation.
- Scanner access was intentionally available only to the guided workflow.
- The remaining generic B608 could reflect scanner conservatism after an allowlist rather than a proven exploitable runtime flaw.
- The frozen success criteria nevertheless required removal of the finding.
- The results should not be generalized directly to large production repositories.

## 10. Human Checkpoint

- The human reviewed the final comparison for factual consistency with both committed result documents.
- Apparent collapsed strings were checked with `Select-String` and confirmed to be terminal-rendering artifacts.
- The comparison explicitly preserved the generic agent's 11-of-11 behavioral success.
- The comparison did not overstate scanner cleanliness as proof of broader model superiority.
- No application, test, evidence JSON, result, protocol, dependency, or configuration file was modified while creating the comparison report.
- The final report was accepted for repository integration.

## 11. Artifacts

- Final comparison: `evaluation/HARD_HOLDOUT_COMPARISON.md`
- Final comparison trajectory: `traces/build/022-hard-holdout-final-comparison.md`
- Protocol: `evaluation/HARD_HOLDOUT_PROTOCOL.md`
- Generic result: `evaluation/runs/baseline_official_03_hard_holdout/RESULT.md`
- SecureAgent-guided result: `evaluation/runs/secureagent_official_01_hard_holdout/RESULT.md`

## 12. Outcome

- The official hard-holdout comparison found a narrowly defined but measurable improvement.
- The generic baseline fully resolved 2 of 3 cases.
- The SecureAgent-guided workflow fully resolved 3 of 3 cases.
- Both workflows passed all 11 behavioral tests.
- The guided workflow removed the one residual required finding.
- The measured improvement was one additional fully resolved case and 33.3 percentage points.
- The result supports SecureAgent as an evidence-driven verification workflow while retaining the finding that the generic agent was highly capable.
- The comparison is ready for the final changelog conclusion and Day 3 completion.
