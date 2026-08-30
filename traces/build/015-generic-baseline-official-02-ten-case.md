# Build Trajectory: Official Ten-Case Generic Baseline

## 1. Metadata

- Date: 2026-08-29
- Repair agent: GitHub Copilot in VS Code Agent mode
- Model policy: Copilot Student Auto model selection
- Underlying automatically selected model: unknown
- Evaluation operator: human evaluator
- Run type: one-pass generic security-repair baseline
- Run directory: `evaluation/runs/baseline_official_02_ten_case`
- Input snapshot commit: `5ef2078`

## 2. Goal

The goal was to measure how well a generic coding agent could repair the same ten-case synthetic security harness without receiving ground-truth metadata, scanner IDs, expected solutions, previous-run information, or SecureAgent-specific guidance.

## 3. Baseline Input Preparation

A fresh run directory was created at `evaluation/runs/baseline_official_02_ten_case`.
Only Python files from the ten committed source fixtures were copied.
The run input contained 34 Python files.
No `ground_truth.json` file was copied.
Pre-run hash comparison checked every copied Python file.
Hash mismatches: 0.
The untouched input snapshot was committed as `5ef2078` with message `test: snapshot official ten-case baseline input`.
The snapshot was pushed to `origin/main`.
GitHub verification confirmed the commit before the repair run.
The repository was clean before the agent started.

## 4. Original Generic Baseline Prompt

```text
Perform one generic security-repair pass on the Python project located at:

evaluation/runs/baseline_official_02_ten_case

Scope and constraints:

- Inspect only files inside this directory.
- Identify and repair security weaknesses while preserving the intended functional behavior.
- Modify only application implementation files.
- Do not modify test files or __init__.py files.
- Do not inspect evaluation/cases, ground-truth files, previous runs, traces, or Git history.
- Do not run Bandit or any other security scanner.
- Do not install packages.
- Use only the existing Python standard library and installed dependencies.
- Complete all repairs in one pass.

After finishing the edits, run exactly this one validation command:

.\.venv\Scripts\python.exe -m pytest evaluation/runs/baseline_official_02_ten_case -q

Do not rerun the command, retry failed repairs, or make any further edits after that validation command, regardless of its result.

Do not commit or push.

Report:
- every file changed,
- a brief description of each repair,
- the exact pytest summary.
```

## 5. Agent Actions

The agent inspected the target run directory and tests, identified the ten weaknesses, and modified exactly these files:

- `evaluation/runs/baseline_official_02_ten_case/case_01/vulnerable_app.py`
- `evaluation/runs/baseline_official_02_ten_case/case_02/vulnerable_app.py`
- `evaluation/runs/baseline_official_02_ten_case/case_03/vulnerable_app.py`
- `evaluation/runs/baseline_official_02_ten_case/case_04/vulnerable_app.py`
- `evaluation/runs/baseline_official_02_ten_case/case_05/vulnerable_app.py`
- `evaluation/runs/baseline_official_02_ten_case/case_06/vulnerable_app.py`
- `evaluation/runs/baseline_official_02_ten_case/case_07/vulnerable_app.py`
- `evaluation/runs/baseline_official_02_ten_case/case_08/vulnerable_app.py`
- `evaluation/runs/baseline_official_02_ten_case/case_09/vulnerable_app.py`
- `evaluation/runs/baseline_official_02_ten_case/case_10/decoder.py`

The repairs were as follows:
- Case 01 used parameterized SQL.
- Case 02 used an argument list with `shell=False`.
- Case 03 read the token from `SECUREAGENT_SERVICE_TOKEN`.
- Case 04 replaced `eval` with restricted AST arithmetic evaluation.
- Case 05 replaced MD5 with SHA-256.
- Case 06 replaced `random.choice` with `secrets.choice`.
- Case 07 added `filter="data"` to archive extraction.
- Case 08 rejected absolute paths and `..` path segments.
- Case 09 added an ownership check and raised `PermissionError` for a non-owner.
- Case 10 replaced pickle decoding with UTF-8 JSON decoding.

No test, `__init__.py`, model, repository, or unrelated application file was modified.

## 6. Agent Validation

The agent ran the required pytest command exactly once.
Agent-reported result: `20 passed in 0.86s`.
The agent made no retry, repair, or edit after that command.
The agent did not run Bandit.
The agent did not install packages, commit, or push.

## 7. Human Checkpoint and Diff Review

The human did not immediately accept the changes.
`git status --short` confirmed exactly ten modified application files.
The complete pending diff was inspected before acceptance.
Every repair matched the intended behavior.
No test or unrelated file was changed.
CRLF-to-LF warnings were recognized as normal Git line-ending notices.
The human then clicked Keep.
A second `git status --short` confirmed the same ten-file scope.
Test integrity was checked independently.
Test files checked: 10.
Test hash mismatches: 0.

## 8. Independent Pytest Evidence

Exact evaluator command:

```powershell
.\.venv\Scripts\python.exe -m pytest evaluation/runs/baseline_official_02_ten_case -q
```

Evidence:
- Independent pytest result: `20 passed in 0.84s`.
- All ten functional tests passed.
- All ten security tests passed.
- No repair, retry, or edit occurred after the agent validation command.

## 9. Independent Bandit Evidence

The evaluator discovered and scanned 13 application Python files.
Test files and `__init__.py` files were excluded.
Raw JSON output was saved at `evaluation/runs/baseline_official_02_ten_case/bandit-results.json`.
Bandit results count: 3.
Bandit exit code: 1 because findings remained.
High-severity findings: 0.
Every required target finding was removed.

| Test ID | Severity | Repository-relative file | Line |
| --- | --- | --- | --- |
| B404 | LOW | `evaluation/runs/baseline_official_02_ten_case/case_02/vulnerable_app.py` | 7 |
| B607 | LOW | `evaluation/runs/baseline_official_02_ten_case/case_02/vulnerable_app.py` | 12 |
| B603 | LOW | `evaluation/runs/baseline_official_02_ten_case/case_02/vulnerable_app.py` | 14 |

The three residual findings are low-severity subprocess-related findings. They do not include the Case 02 target B602, and no new high-severity finding was introduced.

## 10. Final Metrics

- Cases attempted: 10
- Cases resolved: 10
- Case-resolution rate: 100%
- Functional tests passed: 10 of 10
- Security tests passed: 10 of 10
- Required target findings remaining: 0
- New high-severity findings: 0
- Residual low-severity findings: 3
- Retry count after agent validation: 0

## 11. Artifacts

- Repaired baseline: `evaluation/runs/baseline_official_02_ten_case`
- Result summary: `evaluation/runs/baseline_official_02_ten_case/RESULT.md`
- Raw Bandit output: `evaluation/runs/baseline_official_02_ten_case/bandit-results.json`
- Build trajectory: `traces/build/015-generic-baseline-official-02-ten-case.md`

## 12. Outcome

The official generic ten-case baseline resolved all ten cases in one repair pass. Independent evaluation confirmed 20 passing tests and removal of all required target findings. Three low-severity subprocess-related findings remained in Case 02. No new high-severity finding was introduced. The result was accepted as a successful 10-of-10 generic baseline. No later SecureAgent-guided comparison had been performed at this point.
