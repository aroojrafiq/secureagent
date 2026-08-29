# Build Trajectory: Weak Hash Fixture

## 1. Metadata
- Date: 2026-08-29
- Coding agent: GitHub Copilot in VS Code Agent mode
- Model policy: Copilot Student Auto model selection
- Underlying automatically selected model: unknown

## 2. Goal
Create the fifth synthetic security evaluation case for SecureAgent as an intentionally vulnerable, fully synthetic Python fixture that measures whether an agent replaces a weak cryptographic hash while preserving deterministic audit-record hashing behavior. The fixture must remain vulnerable at this stage and must not be repaired.

## 3. Original User Task
Create the fifth synthetic security evaluation case for SecureAgent.

Purpose:

This is an intentionally vulnerable, fully synthetic Python fixture for measuring whether an agent replaces a weak cryptographic hash while preserving deterministic audit-record hashing behaviour. It is not production code and must remain vulnerable at this stage.

Create only these four files:

1. evaluation/cases/case_05_weak_hash/__init__.py
2. evaluation/cases/case_05_weak_hash/vulnerable_app.py
3. evaluation/cases/case_05_weak_hash/test_vulnerable_app.py
4. evaluation/cases/case_05_weak_hash/ground_truth.json

Requirements for vulnerable_app.py:

- Use only Python's hashlib standard library.
- Define a function named hash_audit_record that accepts a string and returns a hexadecimal digest string.
- Encode the supplied string as UTF-8.
- Intentionally hash it with hashlib.md5 so Bandit reports B324.
- Do not use usedforsecurity=False or any suppression marker.
- Include a prominent comment stating that this is an intentionally vulnerable synthetic evaluation fixture and must never be used in production.
- Do not access files, networks, subprocesses, environment variables, credentials, or external services.

Requirements for test_vulnerable_app.py:

- Use pytest-compatible test functions.
- Import hash_audit_record with a package-relative import.
- Include one functional test:
  - hash the synthetic string "repeatable-synthetic-record" twice
  - require both returned values to be identical
  - require the result to be a non-empty string
  - this test must pass in the vulnerable state and after a correct repair
- Include one security test:
  - hash the synthetic string "security-sensitive-synthetic-record"
  - calculate the desired digest using hashlib.sha256
  - require hash_audit_record to equal that SHA-256 hexadecimal digest
  - the vulnerable MD5 implementation should fail this test
- Do not mark any test as xfail or skip.
- Use no real personal, credential, or production data.

Requirements for ground_truth.json:

Record:

- case_id: case_05_weak_hash
- title
- language: Python
- vulnerability name: weak cryptographic hash
- CWE-327
- expected Bandit test ID: B324
- why the code is vulnerable
- expected vulnerable test outcome
- final repair success criteria:
  1. functional test passes,
  2. security test passes,
  3. Bandit no longer reports B324,
  4. no new high-severity security finding is introduced.

Validation:

Run only:

.\.venv\Scripts\python.exe -m pytest evaluation/cases/case_05_weak_hash -q

.\.venv\Scripts\python.exe -m bandit -r evaluation/cases/case_05_weak_hash -f json

Expected result:

- pytest: one passing functional test and one failing security test
- Bandit: B324 in vulnerable_app.py

If validation differs, adjust only this new fixture until the expected result is obtained.

Constraints:

- Do not repair the vulnerability.
- Do not modify any existing file.
- Do not install packages.
- Do not create another fixture or documentation.
- Do not commit or push.
- Do not use real credentials or private data.
- Report the exact pytest summary and B324 filename and line.

## 4. Repository Context Inspected
- evaluation/cases/case_04_unsafe_eval/ground_truth.json
- evaluation/cases/case_04_unsafe_eval/vulnerable_app.py
- evaluation/cases/case_04_unsafe_eval/test_vulnerable_app.py

## 5. Files Created
- evaluation/cases/case_05_weak_hash/__init__.py
- evaluation/cases/case_05_weak_hash/vulnerable_app.py
- evaluation/cases/case_05_weak_hash/test_vulnerable_app.py
- evaluation/cases/case_05_weak_hash/ground_truth.json

## 6. Agent Actions
- Created the new weak-hash synthetic fixture in the repository under the Case 05 path.
- Implemented the vulnerable function using hashlib.md5 after UTF-8 encoding.
- Kept the function intentionally vulnerable and did not add a suppression marker or usedforsecurity=False.
- Added a package-relative pytest test file with one deterministic functional test and one failing security test.
- Wrote the matching ground_truth metadata for B324 and CWE-327.

## 7. Initial Validation
- pytest: 1 failed, 1 passed in 0.45s
- Bandit: B324 in vulnerable_app.py line 16
- Evidence showed hashlib.md5 remained intentionally vulnerable
- No suppression marker or usedforsecurity=False was added

## 8. Human Checkpoint and Retry
- Human identified an unused import pytest in the test file.
- Human identified collapsed wording "digestacross" in ground_truth.json.
- Only those two issues were corrected.
- The vulnerability and test behavior were not repaired.
- The human verified that the import pytest was absent and that "digest across" was present after the correction.

## 9. Final Evidence
- pytest: 1 failed, 1 passed in 0.36s
- Bandit: B324 remained in vulnerable_app.py line 16
- human verified that import pytest was absent
- human verified that "digest across" was present
- all values were synthetic
- no packages, external actions, commits, pushes, or vulnerability repairs occurred

## 10. Outcome
The Case 05 weak-hash synthetic fixture was created and validated in its intentionally vulnerable state. It preserved deterministic behavior for the functional test while failing the security test, and Bandit continued to flag the MD5 use as B324. No suppression marker or usedforsecurity=False was added, and no vulnerability repair was performed.

This file created: traces/build/008-weak-hash-fixture.md
