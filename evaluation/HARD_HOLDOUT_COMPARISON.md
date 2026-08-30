# Official Hard-Holdout Workflow Comparison

## 1. Metadata

- Date: 2026-08-30
- Evaluation: generic one-pass baseline versus SecureAgent-guided workflow
- Protocol: `evaluation/HARD_HOLDOUT_PROTOCOL.md`
- Protocol pre-registration commit: `f402e34`
- Frozen comparison-input commit: `8a1d029`
- Generic baseline result commit: `ff7543a`
- SecureAgent-guided result commit: `be6920b`
- Model policy for both repair runs: GitHub Copilot Student Auto model selection
- Underlying automatically selected model: unknown
- Evaluation operator: human evaluator

## 2. Research Question

The comparison tested whether a structured workflow combining security scanning, agent-blinded evaluator feedback, bounded human approval, and post-repair rescanning could improve complete security-repair outcomes over a one-pass generic coding-agent baseline on byte-identical hard-holdout inputs.

Complete resolution required all public tests, regression tests, and security tests to pass; every pre-registered required scanner target to be removed; no new high-severity finding to appear; and no unauthorized test or package modification.

## 3. Fairness and Input Controls

| Control | Generic baseline | SecureAgent-guided |
| --- | --- | --- |
| Input source | Frozen hard-holdout copy | Same frozen hard-holdout copy |
| Python files | 18 | 18 |
| Ground-truth files copied | 0 | 0 |
| Source-to-run hash mismatches | 0 | 0 |
| Cross-run hash mismatches before repair | 0 | 0 |
| Public tests visible | Yes | Yes |
| Evaluator-test source visible | No | No |
| Evaluator failure output observable | Only final validation output | Pre-repair and post-repair validation output |
| Model policy | Copilot Student Auto | Copilot Student Auto |
| Underlying selected model | Unknown | Unknown |
| Test modification allowed | No | No |
| Package-file modification allowed | No | No |

The inputs, public tests, evaluator tests, success criteria, and model-selection policy were held constant. The intentionally varied factor was workflow access: the generic baseline received one repair pass without scanners or retries, while the guided run used scanning, proposal review, bounded human approval, repair, and rescanning.

## 4. Frozen Vulnerable-State Evidence

- Source pytest pattern: `....F.FF.FF`
- Source pytest result: `5 failed, 6 passed`
- Public tests passing before repair: 3 of 3
- Regression tests passing before repair: 3 of 3
- Security tests failing before repair: 5 of 5
- Source Bandit findings: 1
- Required source finding: B608, MEDIUM, `evaluation/holdout_cases/case_13/query.py`, line 3
- Cases 11 and 12 intentionally produced no Bandit finding.

## 5. Final Quantitative Comparison

| Metric | Generic baseline | SecureAgent-guided | Difference |
| --- | ---: | ---: | ---: |
| Cases attempted | 3 | 3 | 0 |
| Fully resolved cases | 2 | 3 | +1 |
| Full case-resolution rate | 66.7% | 100% | +33.3 percentage points |
| Behaviorally repaired cases | 3 | 3 | 0 |
| Public tests passed | 3 of 3 | 3 of 3 | 0 |
| Agent-blinded regression tests passed | 3 of 3 | 3 of 3 | 0 |
| Agent-blinded security tests passed | 5 of 5 | 5 of 5 | 0 |
| Total post-repair tests passed | 11 of 11 | 11 of 11 | 0 |
| Required findings remaining | 1 | 0 | -1 |
| New high-severity findings | 0 | 0 | 0 |
| Regression failures | 0 | 0 | 0 |
| Initial repair attempts | 1 | 1 | 0 |
| Repair retries after valid verification | 0 | 0 | 0 |
| Unauthorized file modifications | 0 | 0 | 0 |

## 6. Per-Case Comparison

| Case | Generic baseline | SecureAgent-guided | Comparative result |
| --- | --- | --- | --- |
| Case 11: collaborator authorization | All tests passed; no finding expected | All tests passed; no finding expected | Tie: both resolved |
| Case 12: URL allowlist bypass | All tests passed; no finding expected | All tests passed; no finding expected | Tie: both resolved |
| Case 13: dynamic sort injection | All tests passed, but required B608 remained | All tests passed and B608 was removed | Guided workflow fully resolved the frozen criterion |

## 7. Workflow Comparison

| Workflow property | Generic baseline | SecureAgent-guided |
| --- | --- | --- |
| Pre-repair Bandit scan | No | Yes |
| Pre-repair combined evaluator run | No | Yes |
| Explicit repair proposal | No required checkpoint | Yes |
| Human approval before repair | No | Yes |
| Human-bounded file scope | Final diff review only | Approved before editing |
| Post-repair pytest | Yes | Yes |
| Post-repair Bandit | Independent evaluator only | Built into guided verification |
| Raw before-scan artifact | No | Yes |
| Raw after-scan artifact | Yes | Yes |
| Repair retry after valid result | 0 | 0 |
| Invalid tool-execution reruns | 0 | 3 |
| Final test integrity mismatch | 0 | 0 |

The guided run incurred additional operational overhead. Three controlled command reruns were required because Copilot tool invocations produced no valid result, although no source mutation or valid failed verification occurred in those attempts. These reruns are documented separately from repair retries.

## 8. Why the Results Differed

Both workflows recognized and behaviorally repaired all three vulnerability classes. The generic baseline used an allowlist for Case 13 but retained formatted SQL construction. All 11 tests passed, yet Bandit continued to report B608.

The guided workflow saw B608 before repair. During the human checkpoint, the Case 13 authorization was narrowed to literal complete SQL branches or fixed templates without dynamic SQL construction. The final implementation passed the same 11 tests and produced zero Bandit findings.

The measured improvement therefore came from security-verification completeness and residual-finding removal. It did not come from a difference in behavioral test success.

## 9. Interpretation

- The generic agent was strong enough to repair all tested runtime behavior, even on agent-blinded multi-file and semantic holdouts.
- Public plus blinded behavioral tests alone produced a ceiling result for both workflows.
- Scanner verification exposed a remaining pre-registered target that behavioral tests did not distinguish.
- SecureAgent's value in this experiment was the structured evidence loop: scan, test, propose, approve, repair, and rescan.
- Human approval constrained the repair scope and required a scanner-clean SQL construction strategy.
- The comparison supports a measured workflow improvement of one fully resolved case and 33.3 percentage points under the frozen criteria.
- It does not support a broader claim that generic agents cannot repair these vulnerability classes.

## 10. Threats to Validity and Limitations

- The hard holdout contains only three synthetic cases.
- Each workflow was run once, so the comparison does not establish statistical significance or model-level reliability.
- Both runs used Copilot Student Auto selection, but the underlying model was unknown and may not have been identical.
- Evaluator tests were blinded by protocol and file-access restrictions, not cryptographically hidden.
- The guided workflow received scanner access and iterative workflow support by design; this is the intervention being evaluated, not an equal-tooling agent comparison.
- B608 remaining after the generic allowlist may represent scanner conservatism rather than a demonstrably exploitable runtime vulnerability.
- The frozen success criteria nevertheless required removal of the target finding, so Case 13 was consistently scored as incomplete.
- Copilot command-capture failures introduced workflow overhead and required three documented controlled reruns.
- Results from synthetic fixtures may not generalize directly to large production repositories.

## 11. Reproducibility Artifacts

- Pre-registered protocol: `evaluation/HARD_HOLDOUT_PROTOCOL.md`
- Source-harness validation: `traces/build/019-hard-holdout-harness-validation.md`
- Frozen generic input and result: `evaluation/runs/baseline_official_03_hard_holdout`
- Generic result: `evaluation/runs/baseline_official_03_hard_holdout/RESULT.md`
- Generic trajectory: `traces/build/020-generic-hard-holdout-baseline.md`
- Generic Bandit evidence: `evaluation/runs/baseline_official_03_hard_holdout/bandit-results.json`
- Frozen guided input and result: `evaluation/runs/secureagent_official_01_hard_holdout`
- Guided result: `evaluation/runs/secureagent_official_01_hard_holdout/RESULT.md`
- Guided trajectory: `traces/build/021-secureagent-guided-hard-holdout.md`
- Guided pre-repair Bandit evidence: `evaluation/runs/secureagent_official_01_hard_holdout/bandit-before.json`
- Guided post-repair Bandit evidence: `evaluation/runs/secureagent_official_01_hard_holdout/bandit-after-01.json`

## 12. Conclusion

The pre-registered hard-holdout comparison produced a measurable but narrowly defined improvement. The generic baseline fully resolved 2 of 3 cases, while the SecureAgent-guided workflow fully resolved 3 of 3. Both passed all 11 behavioral tests and introduced no high-severity finding or regression. The difference was the removal of Case 13's residual B608 finding through pre-repair scanning, bounded human approval, literal SQL construction, and post-repair rescanning.

The official measured improvement is one additional fully resolved case and 33.3 percentage points. This result supports SecureAgent as an evidence-driven verification workflow while preserving the equally important finding that a capable generic coding agent repaired all tested runtime behavior in one pass.
