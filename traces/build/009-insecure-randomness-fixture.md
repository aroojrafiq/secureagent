# Build Trajectory: Insecure Randomness Fixture

## 1. Metadata
- Date: 2026-08-29
- Coding agent: GitHub Copilot in VS Code Agent mode
- Model policy: Copilot Student Auto model selection
- Underlying automatically selected model: unknown

## 2. Goal
Create a synthetic insecure-randomness evaluation fixture for SecureAgent that remains intentionally vulnerable and demonstrates Bandit B311 while preserving the expected functional behavior.

## 3. Original User Task
Create the sixth synthetic security evaluation case for SecureAgent.

Purpose:
This is an intentionally vulnerable, fully synthetic Python fixture for measuring whether an agent replaces security-sensitive use of Python's predictable random module with the secrets module while preserving behaviour. It is not production code and must remain vulnerable at this stage.

Create only these four files:

1. evaluation/cases/case_06_insecure_randomness/__init__.py
2. evaluation/cases/case_06_insecure_randomness/vulnerable_app.py
3. evaluation/cases/case_06_insecure_randomness/test_vulnerable_app.py
4. evaluation/cases/case_06_insecure_randomness/ground_truth.json

Requirements for vulnerable_app.py:
- Use only the Python standard library.
- Define a function named generate_reset_code that accepts a length integer, defaulting to 12, and returns a string.
- Use a fixed alphabet containing uppercase ASCII letters and decimal digits.
- Intentionally generate the reset code using random.choice so Bandit reports B311.
- Do not use secrets or any suppression marker at this stage.
- Include a prominent comment stating that this is an intentionally vulnerable synthetic evaluation fixture and must never be used in production.
- Do not access files, networks, subprocesses, environment variables, credentials, or external services.
- Use only synthetic values.

Requirements for test_vulnerable_app.py:
- Use pytest-compatible test functions and pytest's monkeypatch fixture where required.
- Import generate_reset_code using a package-relative import.
- Include one functional test:
  - generate a reset code of length 12,
  - require the result to be a string,
  - require its length to equal 12,
  - require every character to belong to uppercase ASCII letters or decimal digits.
  - This test must pass in the vulnerable state and after a correct repair.
- Include one security test:
  - monkeypatch random.choice to return "R",
  - monkeypatch secrets.choice to return "S",
  - call generate_reset_code with length 8,
  - require the returned value to equal "SSSSSSSS".
  - The vulnerable implementation should return "RRRRRRRR" and fail this test.
  - A correct repair using secrets.choice should return "SSSSSSSS" and pass.
- Do not mark any test as xfail or skip.
- Do not generate or use any real credential, token, or personal data.

Requirements for ground_truth.json:
Record:
- case_id: case_06_insecure_randomness
- title
- language: Python
- vulnerability name: insufficiently random security-sensitive value
- CWE-330
- expected Bandit test ID: B311
- why the code is vulnerable
- expected vulnerable test outcome
- final repair success criteria:
  1. functional test passes,
  2. security test passes,
  3. Bandit no longer reports B311,
  4. no new high-severity security finding is introduced.

Validation:
Run only:

.\.venv\Scripts\python.exe -m pytest evaluation/cases/case_06_insecure_randomness -q

.\.venv\Scripts\python.exe -m bandit -r evaluation/cases/case_06_insecure_randomness -f json

Expected result:
- pytest: one passing functional test and one failing security test
- Bandit: B311 in vulnerable_app.py

If validation differs, adjust only this new fixture until the expected result is obtained.

Constraints:
- Do not repair the vulnerability.
- Do not modify any existing file.
- Do not install packages.
- Do not create another fixture or documentation.
- Do not commit or push.
- Do not use real credentials or private data.
- Report the exact pytest summary and B311 filename and line.

## 4. Repository Context Inspected
- evaluation/cases/case_05_weak_hash/vulnerable_app.py
- evaluation/cases/case_05_weak_hash/test_vulnerable_app.py
- evaluation/cases/case_05_weak_hash/ground_truth.json
- traces/build/README.md

## 5. Files Created
- evaluation/cases/case_06_insecure_randomness/__init__.py
- evaluation/cases/case_06_insecure_randomness/vulnerable_app.py
- evaluation/cases/case_06_insecure_randomness/test_vulnerable_app.py
- evaluation/cases/case_06_insecure_randomness/ground_truth.json

## 6. Agent Actions
The agent created the intentionally vulnerable implementation in vulnerable_app.py using the Python standard library and a fixed uppercase/digit alphabet with random.choice, which is the required Bandit B311 pattern. The agent also created the functional pytest test ensuring length and allowed-character validation, plus the monkeypatch-based security test that patches random.choice to return "R" and secrets.choice to return "S" and expects "SSSSSSSS". The ground-truth metadata was recorded with the required case identifier, vulnerability name, CWE-330, expected Bandit ID, and final repair criteria. No vulnerability repair occurred.

## 7. Validation Evidence
- pytest: 1 failed, 1 passed in 0.54s
- Bandit: B311 in vulnerable_app.py line 18
- The functional test passed.
- The security test failed because the vulnerable implementation returned "RRRRRRRR" instead of "SSSSSSSS".
- No real credential, token, personal data, network request, file access, subprocess, or external service was used.

## 8. Human Checkpoint
- The human inspected all four fixture files.
- One collapsed-space wording issue, "thiscode", was identified in descriptive text.
- It was corrected to "this code".
- Select-String verified the corrected wording.
- Executable behavior was unchanged.
- Validation was not rerun because the correction affected descriptive text only.
- The fixture and evidence were accepted.

## 9. Outcome
Case 06 remains intentionally vulnerable, the functional test passes, the security test fails, and Bandit reports B311 at vulnerable_app.py line 18.
