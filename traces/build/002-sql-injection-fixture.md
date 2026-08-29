# Build Trajectory: SQL-Injection Fixture

## 1. Metadata

- Date: 2026-08-29
- Coding agent: GitHub Copilot in VS Code Agent mode
- Model policy: Copilot Student Auto model selection
- The underlying model was selected automatically and is not claimed to be known.

## 2. Goal

Create and validate the first intentionally vulnerable synthetic SQL-injection evaluation case.

## 3. Original User Task

Create the first synthetic security evaluation case for SecureAgent.

Purpose:
This is an intentionally vulnerable, fully synthetic Python fixture used to compare a generic coding-agent baseline against the final SecureAgent workflow. It is not production code and must remain vulnerable at this stage.

Create only these files:

1. evaluation/__init__.py
2. evaluation/cases/__init__.py
3. evaluation/cases/case_01_sql_injection/__init__.py
4. evaluation/cases/case_01_sql_injection/vulnerable_app.py
5. evaluation/cases/case_01_sql_injection/test_vulnerable_app.py
6. evaluation/cases/case_01_sql_injection/ground_truth.json

Requirements for vulnerable_app.py:
- Use only Python's sqlite3 standard library.
- Define a small function that looks up a user by username in a supplied SQLite database path.
- Intentionally construct the SQL query using unsafe string interpolation so that Bandit reports SQL-injection finding B608.
- Return simple user records.
- Include a prominent comment that this is an intentionally vulnerable synthetic evaluation fixture and must never be used in production.
- Do not include credentials, external connections, or personal data.

Requirements for test_vulnerable_app.py:
- Use pytest and a temporary SQLite database.
- Insert exactly two synthetic users.
- Include one functional test showing that an ordinary username lookup works.
- Include one security test using an SQL-injection payload.
- The security test must express the desired secure behaviour: the malicious payload should return no users.
- At the vulnerable-fixture stage, the functional test should pass and the security test should fail. This expected failure is evidence of the planted vulnerability.
- Do not mark the security test as xfail or skip.

Requirements for ground_truth.json:
Record:
- case_id
- title
- language
- vulnerability name
- CWE-89
- expected Bandit test ID B608
- why the code is vulnerable
- the expected vulnerable test outcome
- final repair success criteria:
  1. the security test passes,
  2. the functional test passes,
  3. Bandit no longer reports B608,
  4. no new high-severity security finding is introduced.

Validation:
You may run only these project commands:
- python -m pytest evaluation/cases/case_01_sql_injection -q
- python -m bandit -r evaluation/cases/case_01_sql_injection -f json

The expected validation is:
- pytest: one passing test and one failing security test
- Bandit: at least one B608 finding in vulnerable_app.py

If the expected validation is not obtained, adjust only this fixture until it is obtained.

Constraints:
- Do not repair the vulnerability.
- Do not modify existing files.
- Do not install packages.
- Do not create any other fixture.
- Do not commit or push.
- Do not use real credentials or private data.
- Report the exact test and Bandit outcomes without presenting the intentional failing test as an unexpected project defect.

## 4. Files Created

- `evaluation/__init__.py`
- `evaluation/cases/__init__.py`
- `evaluation/cases/case_01_sql_injection/__init__.py`
- `evaluation/cases/case_01_sql_injection/vulnerable_app.py`
- `evaluation/cases/case_01_sql_injection/test_vulnerable_app.py`
- `evaluation/cases/case_01_sql_injection/ground_truth.json`

## 5. Initial Agent Actions

- Created the three package marker files.
- Created the intentionally vulnerable SQLite application.
- Created the functional and security tests with two synthetic users.
- Created the ground-truth evaluation record.
- Added the missing `pytest` import to the newly created test file.
- No packages were installed.

## 6. Initial Validation Failure

- The first validation commands used `python -m`:
  - `python -m pytest evaluation/cases/case_01_sql_injection -q`
  - `python -m bandit -r evaluation/cases/case_01_sql_injection -f json`
- The agent command environment did not have pytest available: `No module named pytest`.
- The agent command environment did not have Bandit available: `No module named bandit`.
- This does not claim that the project's virtual environment lacked these tools.

## 7. Human Checkpoint and Evidence

- The human reran validation with the explicit `.venv` interpreter.
- Pytest initially failed to collect the tests because of `from vulnerable_app import ...`.
- Bandit successfully found B608 / CWE-89 in `evaluation/cases/case_01_sql_injection/vulnerable_app.py` line 11.
- The human instructed that the import be replaced with a package-relative import.

## 8. Agent Retry

- Corrected the import by changing one line to:
  `from .vulnerable_app import find_users_by_username`
- Ran these exact commands with the explicit virtual-environment interpreter:
  - `\.\.venv\Scripts\python.exe -m pytest evaluation/cases/case_01_sql_injection -q`
  - `\.\.venv\Scripts\python.exe -m bandit -r evaluation/cases/case_01_sql_injection -f json`
- Final pytest result: `1 failed, 1 passed in 0.50s`.
- The failure is the intentionally planted SQL-injection security test: the vulnerable query returns both synthetic users instead of no users.
- Bandit still found B608 / CWE-89 in `evaluation/cases/case_01_sql_injection/vulnerable_app.py` line 11.

## 9. Outcome and Human Approval

- The fixture and validation evidence were reviewed and accepted.
- No commit or push has occurred yet.
