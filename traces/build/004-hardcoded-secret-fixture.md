# Build Trajectory: Hardcoded Secret Fixture

## Metadata
- Date: 2026-08-29
- Tooling: GitHub Copilot in VS Code Agent mode
- Model: Copilot Student Auto model selection
- Note: The automatically selected underlying model is unknown.

## Goal
Create and validate the third intentionally vulnerable synthetic evaluation case for a hardcoded authentication token.

## Original User Task
Create the third synthetic security evaluation case for SecureAgent.

Purpose:
This is an intentionally vulnerable, fully synthetic Python fixture for measuring whether an agent removes a hardcoded authentication token while preserving behaviour. It is not production code and must remain vulnerable at this stage.

Create only these four files:

1. evaluation/cases/case_03_hardcoded_secret/__init__.py
2. evaluation/cases/case_03_hardcoded_secret/vulnerable_app.py
3. evaluation/cases/case_03_hardcoded_secret/test_vulnerable_app.py
4. evaluation/cases/case_03_hardcoded_secret/ground_truth.json

Requirements for vulnerable_app.py:
- Define a clearly synthetic hardcoded authentication token in a module-level variable whose name causes Bandit to report B105.
- The value must be obviously fake and contain no real credential.
- Define a function that builds and returns a Bearer Authorization header using that hardcoded token.
- Include a prominent comment that this is an intentionally vulnerable synthetic evaluation fixture and must never be used in production.
- Do not access networks, files, or external services.

Requirements for test_vulnerable_app.py:
- Use pytest's monkeypatch fixture.
- Import the function using a package-relative import.
- The desired final secure behaviour is to use the environment variable:
  SECUREAGENT_SERVICE_TOKEN
- Include one functional test:
  - set SECUREAGENT_SERVICE_TOKEN to the same synthetic value currently hardcoded,
  - confirm the expected Bearer Authorization header is returned.
  - This test should pass in the vulnerable state and after a correct repair.
- Include one security test:
  - set SECUREAGENT_SERVICE_TOKEN to a different synthetic runtime value,
  - require the returned header to use that runtime value.
  - This test should fail in the vulnerable state because the function ignores the environment.
- Do not mark any test as xfail or skip.
- Use only obviously synthetic token values.

Requirements for ground_truth.json:
Record:
- case_id: case_03_hardcoded_secret
- title
- language
- vulnerability name
- CWE associated with Bandit B105
- expected Bandit test ID B105
- why the code is vulnerable
- expected vulnerable test outcome
- required environment variable name
- final repair success criteria:
  1. functional test passes,
  2. security test passes,
  3. Bandit no longer reports B105,
  4. no secret value is committed,
  5. no new high-severity security finding is introduced.

Validation:
Run only:

.\.venv\Scripts\python.exe -m pytest evaluation/cases/case_03_hardcoded_secret -q

.\.venv\Scripts\python.exe -m bandit -r evaluation/cases/case_03_hardcoded_secret -f json

Expected result:
- pytest: one passing functional test and one failing security test
- Bandit: B105 in vulnerable_app.py

If validation differs, adjust only this new fixture until the expected result is obtained.

Constraints:
- Do not repair the vulnerability.
- Do not modify existing files.
- Do not install packages.
- Do not create other fixtures.
- Do not commit or push.
- Do not use real credentials or private data.
- Report the exact pytest summary and B105 filename and line.

## Files Created
- evaluation/cases/case_03_hardcoded_secret/__init__.py
- evaluation/cases/case_03_hardcoded_secret/vulnerable_app.py
- evaluation/cases/case_03_hardcoded_secret/test_vulnerable_app.py
- evaluation/cases/case_03_hardcoded_secret/ground_truth.json

## Agent Actions and Initial Validation
- Repository-context files the agent verified: README.md, evaluation/README.md, evaluation/cases/__init__.py, evaluation/cases/case_01_sql_injection/vulnerable_app.py, evaluation/cases/case_01_sql_injection/test_vulnerable_app.py, evaluation/cases/case_01_sql_injection/ground_truth.json, evaluation/cases/case_02_command_injection/vulnerable_app.py, evaluation/cases/case_02_command_injection/test_vulnerable_app.py, evaluation/cases/case_02_command_injection/ground_truth.json.
- Created the four fixture files listed above.
- Ran validation commands:
  - .\.venv\Scripts\python.exe -m pytest evaluation/cases/case_03_hardcoded_secret -q
  - .\.venv\Scripts\python.exe -m bandit -r evaluation/cases/case_03_hardcoded_secret -f json
- Initial result: 1 failed, 1 passed in 0.28s.
- Initial Bandit finding: B105 in vulnerable_app.py line 14.
- All tokens were obviously synthetic and no external action occurred.

## Human Checkpoint
Human review found:
- unused import os,
- an inappropriate # noqa: S105 suppression marker,
- ground-truth CWE-798 did not match Bandit's reported CWE-259.

Human-requested corrections:
1. Remove the unused import os from vulnerable_app.py.
2. Remove the inline suppression comment # noqa: S105.
3. Keep the intentionally vulnerable PASSWORD assignment and the synthetic value unchanged.
4. Change ground-truth CWE from CWE-798 to CWE-259.
5. Remove trailing whitespace in the two modified files.
6. Do not otherwise rewrite the content or repair the vulnerability.

## Agent Retry and Final Evidence
- Removed the unused import and suppression marker.
- Changed the ground-truth CWE to CWE-259.
- Kept the synthetic hardcoded PASSWORD intentionally vulnerable.
- Final pytest result: 1 failed, 1 passed in 0.28s.
- Final Bandit result: B105 / CWE-259 in vulnerable_app.py line 12.

## Outcome and Human Approval
- The corrected fixture and evidence were reviewed and accepted.
- No commit or push has occurred yet.

## Pre-commit Formatting Check
- `git diff --cached --check` found trailing whitespace on test-file lines 8 and 13.
- Human review requested a whitespace-only correction.
- The trailing whitespace was removed.
- No test logic or fixture behaviour was changed.
