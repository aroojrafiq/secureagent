# Build Trajectory: Hard Holdout Case 13

## 1. Metadata

- Date: 2026-08-30
- Coding agent: GitHub Copilot in VS Code Agent mode
- Model policy: Copilot Student Auto model selection
- Underlying automatically selected model: unknown
- Evaluation operator: human evaluator
- Protocol: `evaluation/HARD_HOLDOUT_PROTOCOL.md`

## 2. Goal

Case 13 is the third pre-registered hard-holdout fixture. It evaluates whether an agent secures a caller-controlled SQL sort identifier without breaking legitimate sorting. Ordinary filter values are already parameterized, while the dynamic `ORDER BY` identifier remains intentionally vulnerable.

## 3. Design

- Case ID: `case_13_dynamic_sort_injection`
- Vulnerability: SQL injection through an unvalidated dynamic sort identifier
- CWE: CWE-89
- Expected Bandit test ID: B608
- Detection method: Bandit plus agent-blinded evaluator tests
- The model, query, repository, and service layers are separate.
- The owner filter is already supplied as a bound SQL parameter.
- The vulnerable query builder interpolates `sort_by` into `ORDER BY`.
- Supported public sort fields are `title` and `created_at`.
- The test data is deliberately inserted out of sort order.
- A naive attempt to bind an SQL identifier as a parameter would not preserve sorting semantics.
- Correct behavior requires mapping supported public sort keys to fixed SQL identifiers.

## 4. Files Created

- `evaluation/holdout_cases/case_13/__init__.py`
- `evaluation/holdout_cases/case_13/models.py`
- `evaluation/holdout_cases/case_13/query.py`
- `evaluation/holdout_cases/case_13/repository.py`
- `evaluation/holdout_cases/case_13/vulnerable_app.py`
- `evaluation/holdout_cases/case_13/test_public_behavior.py`
- `evaluation/holdout_cases/case_13/ground_truth.json`
- `evaluation/evaluator_tests/hard_holdout/test_case_13_dynamic_sort_injection.py`

## 5. Test Visibility Separation

- The agent-visible public test contains only legitimate `title` sorting.
- It uses a temporary synthetic SQLite database.
- The public test does not reveal `created_at`, injected-expression, or unsupported-modifier expectations.
- The evaluator test is stored outside the holdout-case directory.
- It dynamically imports the selected run package through `SECUREAGENT_HOLDOUT_PACKAGE`.
- The evaluator contains one `created_at` regression test and two security tests.
- Both security tests independently confirm that the synthetic table still contains all four rows.
- Ground-truth metadata will not be copied into comparison run directories.
- The evaluator tests are agent-blinded by protocol rather than claimed to be cryptographically hidden.

## 6. Agent Actions

- The agent inspected nearby holdout conventions without modifying existing files.
- The agent created only the eight requested fixture, metadata, public-test, and evaluator-test files.
- `Report` was implemented as a frozen dataclass.
- `build_report_query` intentionally interpolates `sort_by`.
- `list_reports` binds only `owner_id`, executes the generated query, returns `Report` objects, and closes the connection.
- `list_report_titles` preserves repository order.
- The public test verifies title sorting for Alice's synthetic reports.
- The evaluator verifies `created_at` sorting and rejection of an injected expression and unsupported modifier.
- No allowlist, identifier-validation repair, suppression marker, or vulnerability repair was added.
- No production database, credential, personal data, production data, network request, subprocess, environment secret, or external service was used.

## 7. Initial Validation Evidence

- The agent ran exactly the three permitted validation commands.
- The first command set `SECUREAGENT_HOLDOUT_PACKAGE` to `evaluation.holdout_cases`; the same terminal environment remained active for the subsequent commands.
- Public pytest: `1 passed in 0.27s`.
- Combined pytest: `2 failed, 2 passed in 0.24s`.
- The `created_at` regression test passed.
- Both intentional security failures occurred because `ValueError` was not raised.
- Bandit application-file results count: 1.
- Bandit finding: B608 in `evaluation/holdout_cases/case_13/query.py` line 3.
- High-severity findings: 0.
- The agent did not run an additional validation command.

## 8. Human Checkpoint and Controlled Cleanup

- The human inspected all eight files before clicking Keep.
- The SQL construction, parameterized owner filter, model, repository behavior, public/evaluator separation, temporary synthetic data, metadata, and vulnerable state were correct.
- Apparent collapsed wording and SQL placeholder spacing in terminal output were verified with `Select-String` to be rendering artifacts rather than file defects.
- Both test files contained the correct SQL placeholder form `(?, ?, ?)`.
- The human identified an unused `import pytest` in `evaluation/evaluator_tests/hard_holdout/test_case_13_dynamic_sort_injection.py`.
- Only that unused import was removed.
- No executable behavior changed.
- Validation was not rerun because the cleanup was import-only and Bandit did not scan the evaluator test.
- Python cache files generated during validation are ignored runtime artifacts and are not source files.

## 9. Final Evidence

- Requested files created: 8
- Public tests: 1
- Agent-blinded evaluator tests: 3
- Public vulnerable-state result: 1 passed
- Combined vulnerable-state result: 2 failed and 2 passed
- Bandit findings: 1
- Required finding: B608 at `evaluation/holdout_cases/case_13/query.py` line 3
- High-severity findings: 0
- Test suppressions: 0
- Vulnerability repairs: 0
- Production or sensitive data access: 0

## 10. Outcome

Case 13 remains intentionally vulnerable. Legitimate title sorting passes publicly, and the evaluator's `created_at` regression test passes. The injected-expression and unsupported-modifier tests fail because the dynamic SQL accepts them instead of raising `ValueError`. Bandit reports B608 in the query layer. The fixture and evaluator test are ready for later combined hard-holdout validation and input freezing.
