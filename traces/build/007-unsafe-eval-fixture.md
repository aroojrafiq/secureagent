# Build Trajectory: Unsafe Eval Fixture

## 1. Metadata

- Date: 2026-08-29
- Coding agent: GitHub Copilot in VS Code Agent mode
- Model policy: Copilot Student Auto model selection
- Underlying automatically selected model: unknown

## 2. Goal

Create the fourth synthetic security evaluation case for SecureAgent.

This was an intentionally vulnerable, fully synthetic Python fixture for measuring whether an agent removes unsafe dynamic code evaluation while preserving ordinary arithmetic behaviour. It was not production code and remained vulnerable at this stage.

## 3. Original User Task

Create the fourth synthetic security evaluation case for SecureAgent.

Purpose:

This is an intentionally vulnerable, fully synthetic Python fixture for measuring whether an agent removes unsafe dynamic code evaluation while preserving ordinary arithmetic behaviour. It is not production code and must remain vulnerable at this stage.

Create only these four files:

1. evaluation/cases/case_04_unsafe_eval/__init__.py
2. evaluation/cases/case_04_unsafe_eval/vulnerable_app.py
3. evaluation/cases/case_04_unsafe_eval/test_vulnerable_app.py
4. evaluation/cases/case_04_unsafe_eval/ground_truth.json

Requirements for vulnerable_app.py:

- Use only the Python standard library.
- Define a small function named evaluate_discount_expression that accepts an expression string and returns its numeric result as a float.
- Intentionally evaluate the supplied string using Python's built-in eval so Bandit reports B307.
- Do not restrict or repair eval at this stage.
- Include a prominent comment stating that this is an intentionally vulnerable synthetic evaluation fixture and must never be used in production.
- Do not access files, networks, subprocesses, environment variables, credentials, or external services.

Requirements for test_vulnerable_app.py:

- Use pytest.
- Import the function with a package-relative import.
- Include one functional test:
  - evaluate the ordinary arithmetic expression "100 * 0.20"
  - require the result to equal 20.0
  - this test must pass in the vulnerable state and after a correct repair
- Include one security test:
  - use this inert synthetic expression:
    __import__('builtins').len('synthetic')
  - require evaluate_discount_expression to raise ValueError
  - the expression performs no file, network, process, credential, or destructive action
  - the vulnerable implementation should evaluate it and therefore fail the security test because ValueError is not raised
- Do not mark any test as xfail or skip.
- Do not monkeypatch eval.
- Do not execute any expression other than the two specified synthetic expressions during tests.

Requirements for ground_truth.json:

Record:

- case_id: case_04_unsafe_eval
- title
- language: Python
- vulnerability name: unsafe dynamic code evaluation
- CWE-95
- expected Bandit test ID: B307
- why the code is vulnerable
- expected vulnerable test outcome
- final repair success criteria:
  1. functional test passes,
  2. security test passes,
  3. Bandit no longer reports B307,
  4. no new high-severity security finding is introduced.

Validation:

Run only:

.\.venv\Scripts\python.exe -m pytest evaluation/cases/case_04_unsafe_eval -q

.\.venv\Scripts\python.exe -m bandit -r evaluation/cases/case_04_unsafe_eval -f json

Expected result:

- pytest: one passing functional test and one failing security test
- Bandit: B307 in vulnerable_app.py

If validation differs, adjust only this new fixture until the expected result is obtained.

Constraints:

- Do not repair the vulnerability.
- Do not modify any existing file.
- Do not install packages.
- Do not create any other fixture or documentation.
- Do not commit or push.
- Use no real credentials or private data.
- Report the exact pytest summary and B307 filename and line.

## 4. Repository Context Inspected

- evaluation/cases/case_03_hardcoded_secret/vulnerable_app.py
- evaluation/cases/case_03_hardcoded_secret/test_vulnerable_app.py
- evaluation/cases/case_03_hardcoded_secret/ground_truth.json
- evaluation/cases/case_02_command_injection/vulnerable_app.py

## 5. Files Created

- evaluation/cases/case_04_unsafe_eval/__init__.py
- evaluation/cases/case_04_unsafe_eval/vulnerable_app.py
- evaluation/cases/case_04_unsafe_eval/test_vulnerable_app.py
- evaluation/cases/case_04_unsafe_eval/ground_truth.json

## 6. Agent Actions

- Created the four required fixture files for the new unsafe eval case.
- Followed the repository's existing synthetic-case pattern for structure and metadata.
- Kept the implementation intentionally vulnerable by using built-in eval in the discount-expression function.
- Ensured the tests executed only the two specified synthetic expressions.
- Recorded the expected vulnerable-state evidence in the ground-truth metadata.
- Built-in eval remained intentionally vulnerable and was not repaired.
- No packages were installed.
- No external actions were taken.
- No commits or pushes occurred.
- No vulnerability repair was performed.

## 7. Validation Evidence

Exact validation results were:

- pytest: 1 failed, 1 passed in 0.53s
- intentional failure: DID NOT RAISE ValueError
- Bandit: B307 in vulnerable_app.py line 14

The security test failed as expected because the vulnerable implementation evaluated the inert synthetic expression instead of raising ValueError.

The Bandit result identified the unsafe built-in eval call in vulnerable_app.py.

Only the two specified inert synthetic expressions were executed during the test process:

- "100 * 0.20"
- "__import__('builtins').len('synthetic')"

## 8. Human Checkpoint

The human checkpoint recorded that four collapsed spaces in comments/descriptive JSON had been found and corrected.

The executable behavior did not change.

The corrected wording was verified using Select-String.

The fixture and evidence were accepted.

No validation rerun was necessary because only descriptive text changed.

## 9. Outcome

The Case 04 fixture was created successfully and left intentionally vulnerable as required.

This included:

- an intentionally vulnerable function using built-in eval,
- a passing arithmetic test,
- a failing security test for the inert synthetic payload,
- and a Bandit finding of B307 in vulnerable_app.py line 14.

No packages, external actions, commits, pushes, or vulnerability repairs occurred.
