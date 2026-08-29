# Generic Baseline Official Run 01

**STATUS: VALID PRELIMINARY BASELINE - THREE-CASE BATCH**

## Metadata

- **Date**: 2026-08-29
- **Coding Agent**: GitHub Copilot in VS Code Agent mode
- **Model Policy**: Copilot Student Auto model selection
- **Underlying Model**: Unknown (automatically selected by Copilot Auto)
- **Batch Scope**: Preliminary evidence for current three cases only, not the final ten-case baseline

## Baseline Configuration

The baseline agent received a generic secure-repair task with these constraints:

- Could inspect only the three copied case directories in `evaluation/runs/baseline_official_01/`
- Had no access to ground truth or original fixtures in `evaluation/cases/`
- Could not use Bandit, Semgrep, Gitleaks, or other security scanners
- Made exactly one repair pass
- Ran pytest exactly once
- Made no retry after the test run
- Modified only the three copied `vulnerable_app.py` files
- Did not modify any test files

## Cases Addressed

- case_01 (SQL injection)
- case_02 (command injection)
- case_03 (hardcoded secret)

## Repairs Produced

- **case_01**: Parameterized SQL query (replaced string interpolation)
- **case_02**: argv list with `shell=False` (replaced shell command string)
- **case_03**: `SECUREAGENT_SERVICE_TOKEN` environment variable (replaced hardcoded token)

## Validation Results

### Agent-Run Pytest
**Result**: `6 passed in 0.26s`

### Independent Evaluator Pytest
**Result**: `6 passed in 0.43s`

### Test-Integrity Verification
- case_01 tests unchanged: True
- case_02 tests unchanged: True
- case_03 tests unchanged: True

## Security Scanner Evidence

**Independent Bandit Scan**: `evaluation/runs/baseline_official_01/bandit-results.json`

### Target Vulnerability Status
- **B608** (hardcoded SQL strings): Absent
- **B602** (shell=True): Absent
- **B105** (hardcoded secret): Absent

### Residual Low-Severity Findings
- **B404** (import subprocess): Low severity, case_02
- **B607** (start_process with partial executable path): Low severity, case_02
- **B603** (subprocess with shell parameter): Low severity, case_02

### Severity Summary
- Medium-severity findings: 0
- High-severity findings: 0

## Per-Case Metrics

| Case | Target Found and Removed | Tests Pass | New High-Severity Finding | Metric |
|------|--------------------------|-----------|---------------------------|--------|
| case_01 | Yes | Yes | No | Success |
| case_02 | Yes | Yes | No | Success |
| case_03 | Yes | Yes | No | Success |

## Preliminary Verified Vulnerability Resolution Rate

**3 / 3 = 100%**

## Baseline Composition

This valid preliminary baseline applies only to the current three-case batch. The earlier invalidated run (`baseline_invalidated_01`) is excluded from all metrics.

## Residual Risk Observation

**case_03 Token Handling**: The repair uses `os.environ.get("SECUREAGENT_SERVICE_TOKEN", "")`, which produces an empty-token header when the environment variable is missing. This observed baseline limitation is preserved unchanged for baseline audit integrity.

## Learning and Next Steps

The first three cases are too straightforward to demonstrate an advantage over a generic coding agent. The evaluation must add harder and multi-file cases before final metrics are calculated.

**Current status**: Valid preliminary baseline for three-case batch only. Not the final hackathon baseline.
