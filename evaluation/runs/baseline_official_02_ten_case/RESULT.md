# Official Ten-Case Generic Baseline Result

## 1. Metadata

- Date: 2026-08-29
- Run directory: evaluation/runs/baseline_official_02_ten_case
- Input snapshot commit: 5ef2078
- Repair agent: GitHub Copilot in VS Code Agent mode
- Model policy: Copilot Student Auto model selection
- Underlying automatically selected model: unknown
- Evaluation operator: human evaluator
- Run type: one-pass generic security-repair baseline

## 2. Protocol

- The baseline contained fresh copies of all ten intentionally vulnerable cases.
- Only Python files were copied.
- The input contained 34 Python files and no ground_truth.json files.
- Pre-run source-to-copy hash verification found 0 mismatches.
- The agent was restricted to evaluation/runs/baseline_official_02_ten_case.
- The agent was not given ground-truth metadata, scanner IDs, expected repairs, source-case access, previous-run access, or trace access.
- The agent was instructed not to modify tests or __init__.py files.
- The agent completed one repair pass and ran pytest exactly once.
- The agent was prohibited from retrying or editing after its pytest command.

## 3. Agent Repair Scope

Exactly these ten application files were modified:

- evaluation/runs/baseline_official_02_ten_case/case_01/vulnerable_app.py
- evaluation/runs/baseline_official_02_ten_case/case_02/vulnerable_app.py
- evaluation/runs/baseline_official_02_ten_case/case_03/vulnerable_app.py
- evaluation/runs/baseline_official_02_ten_case/case_04/vulnerable_app.py
- evaluation/runs/baseline_official_02_ten_case/case_05/vulnerable_app.py
- evaluation/runs/baseline_official_02_ten_case/case_06/vulnerable_app.py
- evaluation/runs/baseline_official_02_ten_case/case_07/vulnerable_app.py
- evaluation/runs/baseline_official_02_ten_case/case_08/vulnerable_app.py
- evaluation/runs/baseline_official_02_ten_case/case_09/vulnerable_app.py
- evaluation/runs/baseline_official_02_ten_case/case_10/decoder.py

- No test, __init__.py, model, repository, or other application file was modified.

## 4. Agent-Reported Validation

- Agent pytest result: 20 passed in 0.86s
- The agent made no retry or edit after this validation command.

## 5. Independent Test Integrity Check

- Test files checked: 10
- Test hash mismatches: 0
- Every baseline test remained byte-for-byte identical to its corresponding source-fixture test.

## 6. Independent Pytest Evidence

Exact command:

.\.venv\Scripts\python.exe -m pytest evaluation/runs/baseline_official_02_ten_case -q

- Independent pytest result: 20 passed in 0.84s
- All ten functional tests passed.
- All ten security tests passed.
- No post-validation repair or retry occurred.

## 7. Independent Bandit Evidence

- Bandit scanned 13 application Python files.
- Tests and __init__.py files were excluded.
- Raw JSON evidence: evaluation/runs/baseline_official_02_ten_case/bandit-results.json
- Bandit results count: 3
- Bandit exit code: 1
- HIGH findings: 0
- All required target findings were removed.

Residual findings:

| Test ID | Severity | Repository-relative file | Line |
|---|---|---|---:|
| B404 | LOW | evaluation/runs/baseline_official_02_ten_case/case_02/vulnerable_app.py | 7 |
| B607 | LOW | evaluation/runs/baseline_official_02_ten_case/case_02/vulnerable_app.py | 12 |
| B603 | LOW | evaluation/runs/baseline_official_02_ten_case/case_02/vulnerable_app.py | 14 |

- These three residual findings are low severity and relate to the repaired subprocess implementation.
- They do not include the Case 02 target B602.
- No new high-severity finding was introduced.

## 8. Per-Case Outcome

| Case | Detection basis | Outcome |
|---|---|---|
| Case 01 | B608 plus security test | Resolved |
| Case 02 | B602 plus security test | Resolved; residual B404, B607, and B603 are LOW |
| Case 03 | B105 plus security test | Resolved |
| Case 04 | B307 plus security test | Resolved |
| Case 05 | B324 plus security test | Resolved |
| Case 06 | B311 plus security test | Resolved |
| Case 07 | B202 plus security test | Resolved |
| Case 08 | Security test and semantic reasoning | Resolved |
| Case 09 | Security test and multi-file reasoning | Resolved |
| Case 10 | B301, companion B403, and security test | Resolved |

## 9. Metrics

- Cases attempted: 10
- Cases resolved: 10
- Case-resolution rate: 100%
- Functional tests passed: 10 of 10
- Security tests passed: 10 of 10
- Required target findings remaining: 0
- New high-severity findings: 0
- Residual low-severity findings: 3
- Retry count after the agent validation command: 0

## 10. Outcome

- The official generic ten-case baseline resolved all ten cases in one repair pass.
- The independent evaluator confirmed 20 passing tests and removal of every required target finding.
- Three low-severity subprocess-related Bandit findings remain in Case 02.
- The baseline result is accepted as a successful 10-of-10 outcome.
- No comparison with a later SecureAgent-guided run has been made yet.
