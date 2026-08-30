# Build Trajectory: Official Generic Hard-Holdout Baseline

## 1. Metadata

- Date: 2026-08-30
- Repair agent: GitHub Copilot in VS Code Agent mode
- Model policy: Copilot Student Auto model selection
- Underlying automatically selected model: unknown
- Evaluation operator: human evaluator
- Run type: one-pass generic hard-holdout security-repair baseline
- Run directory: `evaluation/runs/baseline_official_03_hard_holdout`
- Input snapshot commit: `8a1d029`
- Protocol: `evaluation/HARD_HOLDOUT_PROTOCOL.md`

## 2. Goal

The run measured a generic coding agent on three pre-registered hard holdouts using public tests inside the run and agent-blinded evaluator tests outside it. The agent received no scanner access, ground truth, expected solution, retry, or post-validation editing opportunity.

## 3. Frozen Input Preparation

- The source harness was validated before copying.
- The frozen source harness produced 6 passes and 5 intentional failures.
- Source Bandit produced only B608 in Case 13.
- Two fresh comparison directories were created.
- Each directory contained 18 Python files and no `ground_truth.json`.
- Source-to-baseline mismatches: 0.
- Source-to-SecureAgent mismatches: 0.
- Cross-run mismatches: 0.
- The byte-identical comparison inputs were committed as `8a1d029`.
- The repository was clean and synchronized with `origin/main` before the repair run.

## 4. Original Generic Baseline Prompt

The exact generic baseline prompt was:

```text
Perform one generic security-repair pass on the Python project located at:

evaluation/runs/baseline_official_03_hard_holdout

Scope and constraints:

- Inspect only files inside this directory.
- Identify and repair security weaknesses while preserving intended functional behavior.
- Modify only application implementation files.
- Do not modify test_public_behavior.py files or __init__.py files.
- Do not inspect evaluation/evaluator_tests, evaluation/holdout_cases, evaluation/runs/secureagent_official_01_hard_holdout, ground-truth files, protocols, traces, previous runs, Git history, or other chats.
- Do not run Bandit or any other security scanner.
- Do not install packages.
- Use only the existing Python standard library and installed dependencies.
- Complete all repairs in one pass.
- Do not run terminal validation before the final required command.

After finishing the edits, run exactly this one validation command:

$env:SECUREAGENT_HOLDOUT_PACKAGE = "evaluation.runs.baseline_official_03_hard_holdout"; & .\.venv\Scripts\python.exe -m pytest evaluation/runs/baseline_official_03_hard_holdout evaluation/evaluator_tests/hard_holdout -q

After that validation command:

- Do not rerun it.
- Do not retry failed repairs.
- Do not make any further edits.
- Do not run another test or scanner.
- Do not commit or push.

Report:

- every file changed,
- a brief description of each repair,
- the exact pytest progress pattern and summary,
- every failing test and failure reason,
- confirmation that no test or package file was modified.
```

## 5. Agent Actions

Exactly these files were modified:

- `evaluation/runs/baseline_official_03_hard_holdout/case_11/vulnerable_app.py`
- `evaluation/runs/baseline_official_03_hard_holdout/case_12/vulnerable_app.py`
- `evaluation/runs/baseline_official_03_hard_holdout/case_13/query.py`

Repairs:

- Case 11 imported and applied `can_view_workspace`, preserving owner and collaborator access while raising `PermissionError` for outsiders.
- Case 12 used `urllib.parse.urlsplit` and compared scheme, hostname, and port with the configured allowed origin.
- Case 13 mapped `title` and `created_at` through an allowlist and raised `ValueError` for unsupported sort values.
- No test, `__init__.py`, model, repository, policy, configuration, transport, or unrelated application file was modified.

## 6. Agent Validation

- The agent ran the required combined pytest command exactly once.
- Exact progress pattern: `...........`
- Agent result: `11 passed in 0.50s`.
- No test failed.
- No retry, edit, scanner, installation, commit, or push occurred afterward.

## 7. Human Checkpoint and Diff Review

- `git status --short` confirmed exactly three modified application files.
- The complete three-file diff was inspected before acceptance.
- Case 11 correctly reused the existing policy semantics.
- Case 12 replaced prefix validation with parsed origin comparisons.
- Case 13 rejected unsupported values through an allowlist.
- The human recognized that Case 13 still constructed SQL with an f-string and preserved that result for independent scanning instead of changing it.
- The human clicked Keep without requesting a post-validation repair.
- CRLF-to-LF warnings were normal Git line-ending notices.

## 8. Independent Test Integrity and Pytest Evidence

- Public test files checked: 3.
- Public test hash mismatches: 0.
- Independent evaluator command:

```powershell
$env:SECUREAGENT_HOLDOUT_PACKAGE = "evaluation.runs.baseline_official_03_hard_holdout"
& .\.venv\Scripts\python.exe -m pytest evaluation/runs/baseline_official_03_hard_holdout evaluation/evaluator_tests/hard_holdout -q
```

- Exact progress pattern: `...........`
- Independent result: `11 passed in 0.46s`.
- Public tests passed: 3 of 3.
- Agent-blinded regression tests passed: 3 of 3.
- Agent-blinded security tests passed: 5 of 5.
- Regression failures: 0.
- No repair or retry occurred after agent validation.

## 9. Independent Bandit Evidence

- Bandit scanned 11 application Python files.
- Public tests and `__init__.py` files were excluded.
- Raw output: `evaluation/runs/baseline_official_03_hard_holdout/bandit-results.json`.
- Results count: 1.
- Exit code: 1.
- High-severity findings: 0.

| Test ID | Severity | Repository-relative file | Line |
| --- | --- | --- | ---: |
| B608 | MEDIUM | `evaluation/runs/baseline_official_03_hard_holdout/case_13/query.py` | 13 |

- The Case 13 allowlist passed all behavioral tests.
- Bandit still reported required target B608 because the repaired query retained formatted SQL construction.
- The baseline was not edited because retries and post-validation repairs were prohibited.
- Under the frozen success criteria, Case 13 was behaviorally repaired but not fully resolved.
- No new high-severity finding was introduced.

## 10. Final Metrics

- Cases attempted: 3
- Cases fully resolved: 2
- Full case-resolution rate: 2 of 3 (66.7%)
- Behaviorally repaired cases: 3 of 3
- Public tests passed: 3 of 3
- Agent-blinded regression tests passed: 3 of 3
- Agent-blinded security tests passed: 5 of 5
- Total pytest result: 11 of 11 passed
- Required target findings remaining: 1
- New high-severity findings: 0
- Regression failures: 0
- Retry count after agent validation: 0
- Unauthorized file modifications: 0

## 11. Artifacts

- Repaired baseline: `evaluation/runs/baseline_official_03_hard_holdout`
- Result summary: `evaluation/runs/baseline_official_03_hard_holdout/RESULT.md`
- Raw Bandit output: `evaluation/runs/baseline_official_03_hard_holdout/bandit-results.json`
- Build trajectory: `traces/build/020-generic-hard-holdout-baseline.md`

## 12. Outcome

- The generic baseline repaired all tested behavior in one pass.
- Cases 11 and 12 fully satisfied their frozen criteria.
- Case 13 passed all tests but retained B608.
- The official generic hard-holdout resolution rate is therefore 2 of 3 (66.7%).
- This result establishes a measurable verification gap for the later SecureAgent-guided comparison.
- No SecureAgent comparison conclusion has been made yet.
