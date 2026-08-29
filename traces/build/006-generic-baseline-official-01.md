# Generic Baseline Official Run 01

## 1. Metadata

| Field | Value |
|-------|-------|
| **Run ID** | baseline_official_01 |
| **Date** | 2026-08-29 |
| **Agent** | GitHub Copilot in VS Code Agent mode |
| **Model** | Copilot Student Auto (unknown underlying model) |
| **Status** | VALID PRELIMINARY BASELINE - THREE-CASE BATCH |
| **Scope** | Current three cases only, not the final ten-case baseline |

## 2. Goal

Perform a controlled generic baseline evaluation of a coding agent's ability to repair Python security vulnerabilities using a standard secure-repair prompt without access to security scanners, ground truth, or retry capability. Establish preliminary baseline metrics for three corrected evaluation cases.

## 3. Original Baseline Prompt

---

You are performing a controlled generic coding-agent baseline evaluation.

Review and repair any security problems in the Python code located only in these directories:

- evaluation/runs/baseline_official_01/case_01
- evaluation/runs/baseline_official_01/case_02
- evaluation/runs/baseline_official_01/case_03

Make the code secure while preserving its intended behaviour and making the existing tests pass.

Baseline protocol:

- Inspect and edit only files inside the three directories listed above.
- Do not inspect evaluation/cases, any ground_truth.json file, evaluation/runs/baseline_invalidated_01, documentation, traces, Git history, or any other project files.
- Do not use Bandit, Semgrep, Gitleaks, or any other security scanner.
- Do not modify, delete, skip, or mark tests as xfail.
- Do not install dependencies or create additional files.
- Make exactly one repair pass across the three cases.
- After editing, run exactly this one validation command:

  .\.venv\Scripts\python.exe -m pytest evaluation/runs/baseline_official_01 -q

- Do not retry or make further edits after that test command, even if a test fails.
- Do not commit or push.
- Stop after the single test run and report:
  1. files changed,
  2. brief explanation of each repair,
  3. exact pytest summary.

This baseline intentionally excludes specialized scanner findings and a verification-and-retry loop. If repository-wide instructions normally request a security scan, this controlled baseline protocol takes precedence for this run.

---

## 4. Input Preparation

### Fixture Setup
- Fresh copies were made from the three corrected original fixtures in `evaluation/cases/case_01_sql_injection/`, `evaluation/cases/case_02_command_injection/`, and `evaluation/cases/case_03_hardcoded_secret/`
- No ground_truth.json files were copied
- All copies placed in `evaluation/runs/baseline_official_01/case_01/`, `case_02/`, and `case_03/`

### Initial State
- Each case contained a vulnerable `vulnerable_app.py` and `test_vulnerable_app.py`
- All tests were unmodified from corrected originals
- Package marker __init__.py files were present, but no ground_truth.json files or additional evaluation metadata were copied.

## 5. Agent Actions

### Internal Planning
- The baseline agent created three internal todos to organize the work

### Inspection Phase
- Inspected the application and test file in each allowed directory:
  - `evaluation/runs/baseline_official_01/case_01/vulnerable_app.py` and corresponding test
  - `evaluation/runs/baseline_official_01/case_02/vulnerable_app.py` and corresponding test
  - `evaluation/runs/baseline_official_01/case_03/vulnerable_app.py` and corresponding test

### Repair Phase
- Modified only the three copied `vulnerable_app.py` files:
  - **case_01**: Replaced SQL string interpolation with a parameterized query
  - **case_02**: Replaced shell command string with `argv` list and `shell=False`
  - **case_03**: Replaced hardcoded token with `SECUREAGENT_SERVICE_TOKEN` environment variable

### Validation Phase
- Executed the permitted pytest command exactly once
- Command: `.\.venv\Scripts\python.exe -m pytest evaluation/runs/baseline_official_01 -q`

### Compliance
- Did not run a security scanner (Bandit, Semgrep, Gitleaks, or other tools)
- Did not retry after the test run
- Did not commit or push
- Stopped after single test run as instructed

## 6. Files Changed

| File | Change |
|------|--------|
| `evaluation/runs/baseline_official_01/case_01/vulnerable_app.py` | Parameterized SQL query |
| `evaluation/runs/baseline_official_01/case_02/vulnerable_app.py` | argv list with `shell=False` |
| `evaluation/runs/baseline_official_01/case_03/vulnerable_app.py` | `SECUREAGENT_SERVICE_TOKEN` environment variable |

## 7. Agent Validation

**Exact pytest summary from agent run**: `6 passed in 0.26s`

### Test Breakdown
- **Passed**: 6 tests
  - case_01 security test
  - case_01 functional test
  - case_02 security test
  - case_02 functional test
  - case_03 security test
  - case_03 functional test
- **Failed**: 0 tests

All tests passed on the first run with no failures.

## 8. Independent Evaluator Verification

### Pytest Revalidation
The human evaluator re-ran the same test suite on the candidate output:
- **Command**: `.\.venv\Scripts\python.exe -m pytest evaluation/runs/baseline_official_01 -q`
- **Result**: `6 passed in 0.43s`
- **Verification**: All tests passed independently, confirming agent output stability

### Test-Integrity Verification
SHA-256 file-hash comparisons confirmed that all test files remained unchanged:
- case_01 tests unchanged: True
- case_02 tests unchanged: True
- case_03 tests unchanged: True

### Security Scanner Scan
The evaluator, not the baseline agent, ran Bandit afterward to assess residual risk:
- **Tool**: Bandit
- **Scope**: Three candidate `vulnerable_app.py` files only
- **Evidence File**: `evaluation/runs/baseline_official_01/bandit-results.json`

**Target Vulnerability Status**:
- **B608** (hardcoded SQL strings): Absent
- **B602** (shell=True): Absent
- **B105** (hardcoded secret): Absent

**Residual Findings** (low-severity only):
- **B404** (import subprocess): Low severity, case_02
- **B607** (start_process with partial executable path): Low severity, case_02
- **B603** (subprocess with shell parameter): Low severity, case_02

**Severity Summary**:
- Medium-severity findings: 0
- High-severity findings: 0

## 9. Metric Calculation

### Per-Case Criteria
Each case satisfies the predefined metric:
1. Target security finding is removed
2. All tests pass
3. No new high-severity finding is introduced

### Per-Case Results

| Case | Target Removed | Tests Pass | No New High-Severity | Result |
|------|----------------|-----------|----------------------|--------|
| case_01 | Yes | Yes | Yes | Pass |
| case_02 | Yes | Yes | Yes | Pass |
| case_03 | Yes | Yes | Yes | Pass |

### Preliminary Vulnerability Resolution Rate

**Successfully repaired vulnerabilities**: 3
**Total vulnerabilities in batch**: 3
**Preliminary resolution rate**: 3 / 3 = **100%**

### Baseline Status
This preliminary score applies to the current three-case batch only and is not the final ten-case baseline.

## 10. Human Checkpoint

### Review and Acceptance
- The human reviewed the agent's one-pass repairs and candidate output
- All repairs were semantically sound and produced working code
- Independent pytest verification confirmed stability
- Bandit scan confirmed target vulnerabilities were eliminated
- Residual low-severity findings were acceptable and aligned with the repair strategy
- The human accepted the candidate output for recording

### Baseline Integrity
- The invalidated earlier run (`baseline_invalidated_01`) remains explicitly excluded from all metrics
- This result applies only to the current three-case batch
- No metrics are claimed for the final ten-case baseline

### Residual Limitation Documentation
- The empty-token default in case_03 (`os.environ.get("SECUREAGENT_SERVICE_TOKEN", "")`) was recorded as an observed baseline limitation
- This pattern is preserved unchanged for baseline audit integrity
- Not treated as a failure or change to the baseline output

## 11. Limitations and Learning

### Baseline Observation
The first three cases are too straightforward to demonstrate an advantage over a generic coding agent:
- **case_01**: Standard parameterized-query pattern, widely documented and familiar
- **case_02**: Standard `argv` list pattern with `shell=False`, widely documented and familiar
- **case_03**: Standard environment-variable pattern, widely documented and familiar

### Repair Strategy
All three repairs relied on simple, well-established secure patterns that any capable coding assistant can implement without domain-specific knowledge.

### Required Next Steps
To create meaningful baseline differentiation, the evaluation must include:
- Multi-file security defects requiring cross-file reasoning
- Complex control-flow analysis to identify hidden vulnerabilities
- Vulnerability patterns that are less commonly encountered
- Cases requiring security knowledge beyond pattern matching

### Baseline Scope
This result is valid evidence for the current three-case batch only. This preliminary baseline applies only to the current three cases and is not the final ten-case baseline.

## 12. Outcome

**Preliminary Baseline Status**: VALID FOR THREE-CASE BATCH

### Summary
- **Agent one-pass pytest**: 6 passed in 0.26s
- **Independent evaluator pytest**: 6 passed in 0.43s
- **Target Bandit IDs eliminated**: B608, B602, B105
- **Residual low-severity findings**: B404, B607, B603 (case_02 only)
- **High-severity findings**: 0
- **Preliminary resolution rate**: 100% (3/3)

### Next Steps
1. Extend evaluation to include harder and multi-file cases
2. Rerun baseline with the expanded ten-case suite
3. Compare against enhanced agent modes when available
4. Record the final baseline only after full suite validation

### Baseline Metrics
**Current Three-Case Batch**: 100% vulnerability resolution rate
**Final Ten-Case Baseline**: Pending (requires expanded case suite)

**Important**: The invalidated earlier run is excluded from all metrics. This preliminary baseline applies only to the current three cases and is not the final hackathon baseline.
