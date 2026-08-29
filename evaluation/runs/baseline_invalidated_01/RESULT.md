# Generic Baseline Run 01 - Invalidated

**STATUS: INVALIDATED - EXCLUDED FROM ALL METRICS**

## Metadata

- **Date**: 2026-08-29
- **Coding Agent**: GitHub Copilot in VS Code Agent mode
- **Model Policy**: Copilot Student Auto model selection
- **Underlying Model**: Unknown (automatically selected by student mode)

## Baseline Configuration

The baseline agent received only a generic secure-repair task. It was denied:
- Security scanners (Bandit, Semgrep, Gitleaks, or other analysis tools)
- Ground truth access
- Retry capability after initial test run
- Access to original fixtures in `evaluation/cases/`

## Cases Attempted

- case_01
- case_02
- case_03

## Repairs Produced

- **case_01**: Parameterized SQL query (replaced string interpolation)
- **case_02**: `argv` list with `shell=False` (replaced shell command string)
- **case_03**: `SECUREAGENT_SERVICE_TOKEN` environment variable (replaced hardcoded token)

## Validation Result

**Exact pytest summary**: `1 failed, 5 passed in 0.67s`

## Security Scanning

The baseline agent ran no Bandit, Semgrep, Gitleaks, or other security scanner.

## Retry and Editing

The agent made no retry or further edit after the single pytest run.

## Invalidation Reason

A fundamental inconsistency in the Case 02 evaluation harness prevented this run from being used in baseline metrics:

1. The copied Case 02 functional test required the legacy string command: `"nslookup example.test"`
2. The Case 02 security test required a secure `argv` list: `["nslookup", "example.test"]` with `shell=False`
3. A correct repair cannot pass both assertions simultaneously
4. Therefore, this run cannot be attributed to agent capability and is excluded from all metrics

## Corrective Action

1. **Original Fixture Correction**: The original Case 02 functional test in `evaluation/cases/case_02_command_injection/test_vulnerable_app.py` was corrected
2. **Unchanged Elements**: The security test and vulnerable implementation remained unchanged
3. **Revalidation Result**: The corrected original vulnerable fixture produced: `1 failed, 1 passed in 0.32s`
4. **Security Scanner Output**: Bandit reported B602 in `vulnerable_app.py` at line 15
5. **Commit Reference**: Correction was committed as e13dbea
6. **Required Action**: An official baseline rerun is required using the corrected fixture

## Candidate Files

The candidate files in `evaluation/runs/baseline_invalidated_01/` are retained only as audit evidence and must not be used for metrics.
