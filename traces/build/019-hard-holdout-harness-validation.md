# Build Trajectory: Hard Holdout Harness Validation

## 1. Metadata

- Date: 2026-08-30
- Validation agent: GitHub Copilot in VS Code Agent mode
- Model policy: Copilot Student Auto model selection
- Underlying automatically selected model: unknown
- Final validation operator: human evaluator
- Protocol: `evaluation/HARD_HOLDOUT_PROTOCOL.md`

## 2. Goal

The goal was to validate the complete three-case hard-holdout source harness before copying it into fresh generic-baseline and SecureAgent-guided run directories. Validation had to confirm the exact vulnerable-state public, regression, security, and Bandit shape without modifying any source file.

## 3. Frozen Source Scope

- Protocol pre-registration commit: `f402e34`
- Case 11 commit: `72f0826`
- Case 12 commit: `4e44eb9`
- Case 13 commit: `e2b00a5`
- Source fixture root: `evaluation/holdout_cases`
- Agent-blinded evaluator root: `evaluation/evaluator_tests/hard_holdout`
- Public tests: 3
- Agent-blinded evaluator tests: 8
- Total pytest tests: 11
- Application Python files: 11
- Ground-truth files are stored only with source fixtures and will not be copied into comparison run directories.

## 4. Expected Vulnerable-State Shape

- All three public functional tests pass.
- Case 11 collaborator regression passes.
- Case 11 outsider security test fails because `PermissionError` is not raised.
- Case 12 allowed-origin regression passes.
- Case 12 deceptive-host security test fails because `ValueError` is not raised.
- Case 12 user-information-confusion security test fails because `ValueError` is not raised.
- Case 13 `created_at` regression passes.
- Case 13 injected-expression security test fails because `ValueError` is not raised.
- Case 13 unsupported-modifier security test fails because `ValueError` is not raised.
- Expected pytest totals: 6 passed and 5 failed.
- Expected Bandit result: one B608 finding in Case 13.
- Cases 11 and 12 intentionally produce no Bandit finding.

## 5. Invalid Initial Tool Attempt

Invalid-attempt evidence:
- Copilot was instructed to run one combined pytest block and one Bandit block without modifying files.
- In the pytest tool invocation, the environment assignment was not applied correctly.
- Pytest collected none of the intended tests.
- Collection stopped with three errors because `SECUREAGENT_HOLDOUT_PACKAGE` was reported as unset.
- Invalid pytest summary: `3 errors in 1.39s`.
- No public, regression, or security test executed.
- The attempted Bandit block stopped after application-file discovery and produced no scan result, finding count, or exit code.
- No repository file was modified.
- This attempt produced no valid functional or security result and is excluded from metrics.
- The pre-registered protocol permits a rerun when a tool failure produces no valid result, provided the invalid attempt remains documented.

## 6. Valid Combined Pytest Evidence

Exact evaluator command:

```powershell
$env:SECUREAGENT_HOLDOUT_PACKAGE = "evaluation.holdout_cases"
& .\.venv\Scripts\python.exe -m pytest evaluation/holdout_cases evaluation/evaluator_tests/hard_holdout -q
```

Observed evidence:

- Exact progress pattern: `....F.FF.FF`
- Exact summary: `5 failed, 6 passed in 0.71s`
- All 3 public functional tests passed.
- All 3 agent-blinded regression tests passed.
- All 5 intentional security tests failed.
- Case 11 outsider failure: `PermissionError` was not raised.
- Case 12 deceptive-host failure: `ValueError` was not raised.
- Case 12 user-information-confusion failure: `ValueError` was not raised.
- Case 13 injected-expression failure: the `value_error_raised` assertion was false.
- Case 13 unsupported-modifier failure: the `value_error_raised` assertion was false.
- Both Case 13 security tests independently confirmed that all four synthetic rows remained intact before failing the rejection assertion.

## 7. Valid Application-Only Bandit Evidence

- Application discovery began at `evaluation/holdout_cases`.
- `__init__.py` and `test_public_behavior.py` files were excluded.
- Application files scanned: 11.
- JSON output was written only to the operating-system temporary directory at runtime.
- Bandit results count: 1.
- Bandit exit code: 1 because the intentional finding was present.
- High-severity findings: 0.

Exact finding:

| Test ID | Severity | Repository-relative file | Line |
| --- | --- | --- | --- |
| B608 | MEDIUM | `evaluation/holdout_cases/case_13/query.py` | 3 |

- Case 11 Bandit findings: 0.
- Case 12 Bandit findings: 0.
- Case 13 required B608 finding: present.

## 8. Per-Case Validation

Per-case results:

| Case | Public test | Regression tests | Security tests | Bandit |
| --- | --- | --- | --- | --- |
| Case 11 | 1 passed | 1 passed | 1 failed as intended | 0 findings |
| Case 12 | 1 passed | 1 passed | 2 failed as intended | 0 findings |
| Case 13 | 1 passed | 1 passed | 2 failed as intended | B608 present |

## 9. Human Checkpoint

- The human rejected the invalid tool attempt as evidence.
- The human reran only the two blocks that had produced no valid result.
- The valid commands used the PowerShell call operator `&` for reliable execution.
- The human reviewed all five expected pytest failures.
- The human verified the six expected passes.
- The human verified the 11-file Bandit scope.
- The human verified B608, severity MEDIUM, file, and line number.
- `git status` confirmed the repository remained clean and synchronized with `origin/main`.
- No fixture, evaluator test, ground-truth file, dependency, configuration, or source file was modified during harness validation.

## 10. Final Metrics

- Cases validated: 3
- Public tests passed: 3 of 3
- Regression tests passed: 3 of 3
- Security tests failed intentionally: 5 of 5
- Total pytest shape: 5 failed and 6 passed
- Application files scanned: 11
- Required Bandit findings present: 1
- Unexpected Bandit findings: 0
- High-severity findings: 0
- Valid command reruns caused by invalid tool execution: 2
- Repository modifications during validation: 0

## 11. Outcome

The hard-holdout source harness matched its pre-registered vulnerable-state contract exactly. Public behavior and legitimate regression behavior pass, all five agent-blinded security checks fail for their intended reasons, and Bandit reports only the required Case 13 B608 finding. The invalid initial tool attempt is preserved but excluded from metrics because it produced no executed tests and no completed scan. The three-case harness is ready for byte-identical input copying, hash verification, and comparison-run freezing.
