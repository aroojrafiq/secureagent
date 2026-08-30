# Official Hard-Holdout Generic Baseline Result

## 1. Metadata

- Date: 2026-08-30
- Run directory: `evaluation/runs/baseline_official_03_hard_holdout`
- Input snapshot commit: `8a1d029`
- Repair agent: `GitHub Copilot in VS Code Agent mode`
- Model policy: `Copilot Student Auto model selection`
- Underlying automatically selected model: `unknown`
- Evaluation operator: `human evaluator`
- Run type: `one-pass generic hard-holdout security-repair baseline`
- Protocol: `evaluation/HARD_HOLDOUT_PROTOCOL.md`

## 2. Protocol

- The baseline received byte-identical Python copies of Cases 11, 12, and 13.
- The run contained 18 Python files and no `ground_truth.json` files.
- Source-to-baseline, source-to-SecureAgent, and cross-run hash mismatches were all 0 before either repair run.
- The agent was restricted to `evaluation/runs/baseline_official_03_hard_holdout`.
- The agent was prohibited from inspecting evaluator-test source, source holdouts, the SecureAgent run, ground truth, protocols, traces, prior runs, Git history, or other chats.
- The agent could inspect public tests inside its run directory.
- The agent was prohibited from using Bandit or another scanner.
- It received one repair pass and one final pytest command.
- It could not retry, edit, or run another command after validation.

## 3. Agent Repair Scope

Exactly these three application files were modified:

- `evaluation/runs/baseline_official_03_hard_holdout/case_11/vulnerable_app.py`
- `evaluation/runs/baseline_official_03_hard_holdout/case_12/vulnerable_app.py`
- `evaluation/runs/baseline_official_03_hard_holdout/case_13/query.py`

Repairs:

- Case 11 applied `can_view_workspace` before returning document content, preserving owner and collaborator access while rejecting outsiders.
- Case 12 parsed the requested and allowed URLs and compared scheme, hostname, and port instead of using a raw prefix check.
- Case 13 mapped supported sort keys through an allowlist and raised `ValueError` for unsupported values.

No public test, `__init__.py` file, model, repository, policy, configuration, transport, or other application file was modified.

## 4. Agent-Reported Validation

- Exact progress pattern: `...........`
- Agent pytest result: `11 passed in 0.50s`
- No test failed.
- The agent made no retry or edit after validation.
- The agent did not run Bandit or another scanner.

## 5. Independent Test Integrity Check

- Public test files checked: `3`
- Public test hash mismatches: `0`
- All public tests remained byte-for-byte identical to their source-fixture counterparts.
- Git status confirmed that only the three application files were modified before independent evidence was generated.

## 6. Independent Pytest Evidence

Exact evaluator command:

```powershell
$env:SECUREAGENT_HOLDOUT_PACKAGE = "evaluation.runs.baseline_official_03_hard_holdout"
& .\.venv\Scripts\python.exe -m pytest evaluation/runs/baseline_official_03_hard_holdout evaluation/evaluator_tests/hard_holdout -q
```

Evidence:

- Exact progress pattern: `...........`
- Independent pytest result: `11 passed in 0.46s`
- Public functional tests passed: `3 of 3`
- Agent-blinded regression tests passed: `3 of 3`
- Agent-blinded security tests passed: `5 of 5`
- Regression failures: `0`
- No post-validation repair or retry occurred.

## 7. Independent Bandit Evidence

- Bandit scanned 11 application Python files.
- Public tests and `__init__.py` files were excluded.
- Raw evidence: `evaluation/runs/baseline_official_03_hard_holdout/bandit-results.json`
- Bandit results count: `1`
- Bandit exit code: `1`
- High-severity findings: `0`

| Test ID | Severity | Repository-relative file | Line |
| --- | --- | --- | ---: |
| `B608` | `MEDIUM` | `evaluation/runs/baseline_official_03_hard_holdout/case_13/query.py` | `13` |

- Case 13’s allowlist repair passed all behavioral tests.
- Bandit still reported the pre-registered required target `B608` because the repaired query continued to use formatted SQL construction.
- The baseline was not edited after this finding because the protocol prohibited retries and post-validation repairs.
- This remaining required finding means Case 13 does not satisfy the frozen full-resolution criteria.
- No new high-severity finding was introduced.

## 8. Per-Case Outcome

| Case | Public and evaluator behavior | Bandit requirement | Final outcome |
| --- | --- | --- | --- |
| Case 11 | All tests passed | No finding expected | Resolved |
| Case 12 | All tests passed | No finding expected | Resolved |
| Case 13 | All tests passed | Required `B608` remained | Behaviorally repaired but not fully resolved |

## 9. Metrics

- Cases attempted: `3`
- Cases fully resolved: `2`
- Full case-resolution rate: `2 of 3 (66.7%)`
- Behaviorally repaired cases: `3 of 3`
- Public tests passed: `3 of 3`
- Agent-blinded regression tests passed: `3 of 3`
- Agent-blinded security tests passed: `5 of 5`
- Total tests passed: `11 of 11`
- Required target findings remaining: `1`
- New high-severity findings: `0`
- Regression failures: `0`
- Retry count after agent validation: `0`
- Unauthorized file modifications: `0`

## 10. Outcome

- The generic baseline correctly repaired the observable behavior of all three hard-holdout cases in one pass.
- Cases 11 and 12 fully satisfied their frozen success criteria.
- Case 13 passed every public and blinded evaluator test but retained required Bandit finding `B608`.
- Therefore, the official full-resolution score is `2 of 3 (66.7%)`, while behavioral test success is `11 of 11`.
- The unresolved scanner target is preserved as honest baseline evidence.
- No comparison conclusion with the SecureAgent-guided run has been made yet.
