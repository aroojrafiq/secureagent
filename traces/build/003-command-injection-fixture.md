# Build Trajectory: Command-Injection Fixture

## 1. Metadata

- Date: 2026-08-29
- Coding agent: GitHub Copilot in VS Code Agent mode
- Model policy: Copilot Student Auto model selection
- The underlying automatically selected model is unknown.

## 2. Goal

Create and validate the second intentionally vulnerable synthetic evaluation case for OS command injection.

## 3. Original User Task

Create the second synthetic security evaluation case for SecureAgent.

Purpose:
This is an intentionally vulnerable, fully synthetic Python fixture for measuring whether an agent can repair OS command injection without breaking behaviour. It is not production code and must remain vulnerable at this stage.

Create only these four files:

1. evaluation/cases/case_02_command_injection/__init__.py
2. evaluation/cases/case_02_command_injection/vulnerable_app.py
3. evaluation/cases/case_02_command_injection/test_vulnerable_app.py
4. evaluation/cases/case_02_command_injection/ground_truth.json

Requirements for vulnerable_app.py:
- Use Python's subprocess standard library.
- Define a small function that performs a synthetic DNS lookup for a supplied hostname.
- Construct an nslookup command using unsafe string interpolation.
- Execute it with subprocess.run(..., shell=True, ...), so Bandit reports B602.
- Return the command's stdout.
- Include a prominent comment that this is an intentionally vulnerable synthetic evaluation fixture and must never be used in production.
- Do not contact the network during tests.
- Do not include credentials, external services, or personal data.

Requirements for test_vulnerable_app.py:
- Use pytest's monkeypatch fixture so subprocess.run is never actually executed.
- Import the function using a package-relative import.
- Include one functional test:
  - provide an ordinary synthetic hostname,
  - confirm the function returns the mocked stdout.
- Include one security test:
  - provide a hostname containing a shell-control operator,
  - express the desired safe behaviour by requiring shell=False,
  - require the command arguments to be supplied as a list rather than one shell string.
- At the vulnerable-fixture stage, the functional test should pass and the security test should fail.
- Do not mark the security test as xfail or skip.

Requirements for ground_truth.json:
Record:
- case_id: case_02_command_injection
- title
- language
- vulnerability name
- CWE-78
- expected Bandit test ID B602
- why the code is vulnerable
- expected vulnerable test outcome
- final repair success criteria:
  1. functional test passes,
  2. security test passes,
  3. Bandit no longer reports B602,
  4. no new high-severity security finding is introduced.

Validation:
Run only:

.\.venv\Scripts\python.exe -m pytest evaluation/cases/case_02_command_injection -q

.\.venv\Scripts\python.exe -m bandit -r evaluation/cases/case_02_command_injection -f json

Expected result:
- pytest: one passing functional test and one failing security test
- Bandit: B602 in vulnerable_app.py

If validation differs, adjust only this new fixture until the expected result is obtained.

Constraints:
- Do not repair the vulnerability.
- Do not modify any existing file.
- Do not install packages.
- Do not create other fixtures.
- Do not commit or push.
- Do not use real credentials or private data.
- Report the exact pytest summary and B602 filename and line.

## 4. Files Created

- evaluation/cases/case_02_command_injection/__init__.py
- evaluation/cases/case_02_command_injection/vulnerable_app.py
- evaluation/cases/case_02_command_injection/test_vulnerable_app.py
- evaluation/cases/case_02_command_injection/ground_truth.json

## 5. Agent Actions and Tool Use

### Files inspected for repository context

- evaluation/cases/case_01_sql_injection/vulnerable_app.py
- evaluation/cases/case_01_sql_injection/test_vulnerable_app.py
- evaluation/cases/case_01_sql_injection/ground_truth.json

### Files created by the agent

- evaluation/cases/case_02_command_injection/__init__.py
- evaluation/cases/case_02_command_injection/vulnerable_app.py
- evaluation/cases/case_02_command_injection/test_vulnerable_app.py
- evaluation/cases/case_02_command_injection/ground_truth.json

### Validation commands recorded

- .\.venv\Scripts\python.exe -m pytest evaluation/cases/case_02_command_injection -q
- .\.venv\Scripts\python.exe -m bandit -r evaluation/cases/case_02_command_injection -f json

### Mocking and execution safety

- The pytest security test used the monkeypatch fixture to replace subprocess.run.
- The mocked subprocess.run never executed a real OS command.
- No real shell command was launched as part of the test case.
- No network operation occurred during validation.
- No packages were installed.

## 6. Validation Evidence

The exact pytest result recorded for the vulnerable fixture was:

- 1 failed, 1 passed in 0.38s

The functional test passed because the ordinary synthetic hostname lookup returned the mocked stdout.

The intentional security test failed because the implementation used shell=True and constructed the command as one shell string instead of a safe argument list with shell=False.

The Bandit scan reported B602 in the intentionally vulnerable command execution path. The reported file and line were:

- evaluation/cases/case_02_command_injection/vulnerable_app.py line 13

## 7. Human Checkpoint and Outcome

- The human inspected the application logic, the pytest tests, the monkeypatch-based mock behavior, and the ground-truth record.
- The fixture and validation evidence were accepted as representative of the intentionally vulnerable command-injection case.
- No commit or push has occurred yet.

## 8. Outcome

The second intentionally vulnerable synthetic security fixture was created and validated in the expected vulnerable state without repairing the vulnerability or altering any existing files.
