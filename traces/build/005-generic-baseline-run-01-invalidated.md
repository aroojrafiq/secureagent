# Generic Baseline Run 01 - Invalidated

## 1. Metadata

| Field | Value |
|-------|-------|
| **Run ID** | baseline_invalidated_01 |
| **Date** | 2026-08-29 |
| **Agent** | GitHub Copilot in VS Code Agent mode |
| **Model** | Copilot Student Auto (unknown underlying model) |
| **Status** | INVALIDATED - EXCLUDED FROM ALL METRICS |

## 2. Goal

Perform a controlled generic baseline evaluation of a coding agent's ability to repair Python security vulnerabilities without access to specialized security scanners, ground truth, or retry capability. The agent was tasked with making code secure while preserving intended behavior and passing existing tests.

## 3. Original Baseline Prompt

---

You are performing a controlled generic coding-agent baseline evaluation.

Review and repair any security problems in the Python code located only in these directories:

- evaluation/runs/baseline/case_01
- evaluation/runs/baseline/case_02
- evaluation/runs/baseline/case_03

Make the code secure while preserving its intended behaviour and making the existing tests pass.

Baseline protocol:

- Inspect and edit only files inside the three directories listed above.
- Do not inspect evaluation/cases, ground_truth.json, documentation, traces, Git history, or any other project files.
- Do not use Bandit, Semgrep, Gitleaks, or any other security scanner.
- Do not modify, delete, skip, or mark tests as xfail.
- Do not install dependencies or create additional files.
- Make exactly one repair pass across the three cases.
- After editing, run exactly this one validation command:

  .\.venv\Scripts\python.exe -m pytest evaluation/runs/baseline -q

- Do not retry or make further edits after that test command, even if a test fails.
- Do not commit or push.
- Stop after the single test run and report:
  1. files changed,
  2. brief explanation of each repair,
  3. exact pytest summary.

This baseline intentionally excludes specialized scanner findings and a verification-and-retry loop. If repository-wide instructions normally request a security scan, this controlled baseline protocol takes precedence for this run.

---

## 4. Agent Actions

The agent followed the baseline protocol and executed the following observed actions:

### Inspection Phase
- Inspected the application and test file in each of the three allowed case directories:
  - `evaluation/runs/baseline/case_01/vulnerable_app.py` and corresponding test
  - `evaluation/runs/baseline/case_02/vulnerable_app.py` and corresponding test
  - `evaluation/runs/baseline/case_03/vulnerable_app.py` and corresponding test

### Repair Phase
- Modified only the three `vulnerable_app.py` copies:
  - **case_01**: Replaced SQL string interpolation with a parameterized query
  - **case_02**: Replaced the shell command string with an `argv` list and `shell=False`
  - **case_03**: Replaced hardcoded token with `SECUREAGENT_SERVICE_TOKEN` environment variable

### Validation Phase
- Executed the permitted pytest command exactly once
- Command: `.\.venv\Scripts\python.exe -m pytest evaluation/runs/baseline -q`

### Compliance
- Did not run a security scanner (Bandit, Semgrep, Gitleaks, or other tools)
- Did not retry after the test failure
- Did not commit or push
- Stopped after single test run as instructed

## 5. Files Changed

| File | Change |
|------|--------|
| `evaluation/runs/baseline/case_01/vulnerable_app.py` | Parameterized SQL query |
| `evaluation/runs/baseline/case_02/vulnerable_app.py` | argv list with `shell=False` |
| `evaluation/runs/baseline/case_03/vulnerable_app.py` | `SECUREAGENT_SERVICE_TOKEN` environment variable |

## 6. Agent Validation

**Exact pytest summary**: `1 failed, 5 passed in 0.67s`

### Test Breakdown
- **Passed**: 5 tests
  - case_01 security test
  - case_01 functional test
  - case_02 security test
  - case_03 security test
  - case_03 functional test
- **Failed**: 1 test
  - case_02 functional test

### Failure Root Cause
The copied Case 02 functional test expected the legacy command string `"nslookup example.test"` but the agent's secure repair provided an `argv` list `["nslookup", "example.test"]` with `shell=False`. The test contract was internally inconsistent and could not be satisfied by a correct secure repair.

## 7. Human Checkpoint

### Review Decision
The human reviewer:
- Reviewed the reported repairs and preserved the one-pass candidate outputs for audit evidence
- Identified that the test failure was caused by a harness defect, not an agent failure
- Recognized that the Case 02 functional test did not permit the documented secure repair
- Directed and approved a correction to the original Case 02 fixture

### Evidence Collection
- Renamed the run directory from `baseline` to `baseline_invalidated_01`
- Retained all candidate files for audit evidence
- Documented the decision and corrective action

## 8. Invalidation Decision

**Decision**: INVALIDATED - EXCLUDED FROM ALL METRICS

**Rationale**:

The baseline run cannot be used in official metrics because the Case 02 evaluation harness contained an internal contradiction:

1. **Functional Test Requirement**: The test expected a shell command string: `"nslookup example.test"`
2. **Security Test Requirement**: The test required a secure `argv` list with `shell=False`
3. **Constraint Violation**: These requirements are mutually exclusive under the agent's repair strategy
4. **Metric Impact**: The test failure cannot be attributed to agent capability because the harness itself prevented a correct solution

### Metric Impact
- Run cannot be included in baseline success rate calculations
- Run cannot be included in security repair effectiveness metrics
- Run cannot be used for agent capability assessment

## 9. Corrective Action

### Original Fixture Correction
The human directed and approved the following corrective actions on the original fixture in `evaluation/cases/case_02_command_injection/`:

1. **Test Correction**: Updated `evaluation/cases/case_02_command_injection/test_vulnerable_app.py` to permit the secure argv-based repair
2. **Implementation Unchanged**: Left `evaluation/cases/case_02_command_injection/vulnerable_app.py` and its security test unchanged

### Revalidation
- **Command**: `.\.venv\Scripts\python.exe -m pytest evaluation/cases/case_02_command_injection -q`
- **Result**: `1 failed, 1 passed in 0.32s`
- **Functional Test**: Passed because the ordinary lookup returned the mocked stdout
- **Security Test**: Failed because the intentionally vulnerable implementation still used a shell command string with shell=True

### Security Scanner Verification
- **Tool**: Bandit
- **Output**: B602 (shell=True usage) in `vulnerable_app.py` at line 15
- **Status**: Correct detection of remaining vulnerability in unfixed code

### Commit Record
- **Commit**: e13dbea
- **Purpose**: Corrected original Case 02 fixture to permit secure repair

### Next Steps
- An official baseline rerun is required using the corrected fixture
- Fresh copies from `evaluation/cases/` must be used
- The baseline_invalidated_01 run must be excluded from all metrics and analysis

## 10. Learning

### Key Insight
A baseline failure is not automatically an agent failure. Evaluation harnesses must have internally consistent test contracts that permit documented secure repairs to pass all assertions.

### Process Improvement
- **Test Design**: Ensure that both functional and security tests can be satisfied by the documented secure repair
- **Harness Validation**: Validate test contracts before recording baseline metrics
- **Human Review**: A human checkpoint before metric recording can catch harness defects
- **Evidence Preservation**: Retained copies serve as audit evidence for reproducibility and process analysis

### Baseline Quality
- The original Case 02 harness defect was identified before metrics were recorded
- The correction ensures that future baseline runs have valid, internally consistent test contracts
- Agent capability metrics will be more reliable with validated harnesses

### Official Baseline Status
The official baseline has not yet been recorded. Rerun is required with the corrected fixture.
