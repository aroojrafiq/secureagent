# Build Trajectory: Unsafe Deserialization Fixture

## 1. Metadata
- Date: 2026-08-29
- Coding agent: GitHub Copilot in VS Code Agent mode
- Model policy: Copilot Student Auto model selection
- Underlying automatically selected model: unknown

## 2. Goal
This is the tenth synthetic case and a multi-file decoder/service fixture for unsafe pickle deserialization.

## 3. Original User Task
Create the tenth synthetic security evaluation case for SecureAgent.

Purpose:
This is an intentionally vulnerable, fully synthetic multi-file Python fixture for measuring whether an agent replaces unsafe pickle deserialization with safe JSON parsing while preserving behaviour across a decoder and service layer. It is not production code and must remain vulnerable at this stage.

Create only these five files:

1. evaluation/cases/case_10_unsafe_deserialization/__init__.py
2. evaluation/cases/case_10_unsafe_deserialization/decoder.py
3. evaluation/cases/case_10_unsafe_deserialization/vulnerable_app.py
4. evaluation/cases/case_10_unsafe_deserialization/test_vulnerable_app.py
5. evaluation/cases/case_10_unsafe_deserialization/ground_truth.json

Requirements for decoder.py:
- Use only the Python standard library.
- Import pickle.
- Define decode_profile_payload(payload: bytes) -> dict[str, str].
- Intentionally return pickle.loads(payload) so Bandit reports B301.
- Do not use json in the vulnerable implementation.
- Do not add nosec, noqa, or any suppression marker.
- Include a prominent comment stating that this is an intentionally vulnerable synthetic evaluation fixture and must never be used in production.
- Do not access files, networks, subprocesses, environment variables, credentials, or external services.

Requirements for vulnerable_app.py:
- Import decode_profile_payload using a package-relative import.
- Define get_profile_name(payload: bytes) -> str.
- Decode the payload through decode_profile_payload.
- Return the decoded mapping's "name" value.
- Do not deserialize directly in this service module.
- Do not repair the decoder.

Requirements for test_vulnerable_app.py:
- Use pytest-compatible tests and pytest's monkeypatch fixture.
- Import json and pickle only so their loads functions can be safely monkeypatched.
- Import get_profile_name using a package-relative import.
- Never pass a real pickle payload to pickle.loads.
- Include one functional test:
  - use the synthetic JSON bytes payload b'{"name":"synthetic-user"}',
  - monkeypatch pickle.loads to return {"name": "synthetic-user"} without deserializing anything,
  - call get_profile_name,
  - require the result to equal "synthetic-user".
  - This test must pass in the vulnerable state and after a correct repair using json.loads.
- Include one security test:
  - use the same inert synthetic JSON bytes payload,
  - monkeypatch pickle.loads to record that it was called and return {"name": "pickle-path"},
  - monkeypatch json.loads to record that it was called and return {"name": "json-path"},
  - call get_profile_name,
  - require the result to equal "json-path",
  - require json.loads to have been called,
  - require pickle.loads not to have been called.
  - The vulnerable implementation should return "pickle-path" and fail.
  - A correct repair using json.loads should return "json-path" and pass.
- Do not mark any test as xfail or skip.
- Do not perform real unsafe deserialization.
- Use no real personal, credential, production, or private data.

Requirements for ground_truth.json:
Record:
- case_id: case_10_unsafe_deserialization
- title
- language: Python
- vulnerability name: deserialization of untrusted data
- cwe: CWE-502
- expected_bandit_test_id: B301
- expected_companion_bandit_test_ids:
  - B403
- detection_method: Bandit plus pytest security test
- why the code is vulnerable
- expected vulnerable test outcome
- relevant application files:
  - decoder.py
  - vulnerable_app.py
- final repair success criteria:
  1. functional test passes,
  2. security test passes,
  3. Bandit no longer reports B301,
  4. the unsafe pickle import and B403 companion finding are removed,
  5. no new high-severity security finding is introduced.

Validation:
Run only these two commands:

.\.venv\Scripts\python.exe -m pytest evaluation/cases/case_10_unsafe_deserialization -q

.\.venv\Scripts\python.exe -m bandit evaluation/cases/case_10_unsafe_deserialization/decoder.py evaluation/cases/case_10_unsafe_deserialization/vulnerable_app.py -f json

Expected result:
- pytest: one passing functional test and one failing security test
- the security test fails because the vulnerable implementation uses the mocked pickle path instead of the mocked JSON path
- Bandit reports target B301 in decoder.py
- Bandit also reports companion B403 for the pickle import
- Bandit results count: 2
- no high-severity finding is expected
- No real pickle payload is deserialized during testing.

If validation differs, adjust only this new fixture until the expected result is obtained.

Constraints:
- Do not repair the vulnerability.
- Do not modify any existing file.
- Do not install packages.
- Do not create another fixture or documentation.
- Do not add nosec, noqa, or any suppression marker.
- Do not run any additional validation command.
- Do not commit or push.
- Do not use real credentials, personal data, production data, or private data.
- Report the exact pytest summary, Bandit results count, and B301/B403 filenames and lines.

## 4. Repository Context Inspected
- evaluation/cases/case_08_path_traversal/test_vulnerable_app.py
- evaluation/cases/case_08_path_traversal/ground_truth.json
- evaluation/cases/case_09_missing_authorization/vulnerable_app.py
- evaluation/cases/case_09_missing_authorization/test_vulnerable_app.py
- evaluation/cases/case_09_missing_authorization/ground_truth.json

## 5. Files Created
- `evaluation/cases/case_10_unsafe_deserialization/__init__.py`
- `evaluation/cases/case_10_unsafe_deserialization/decoder.py`
- `evaluation/cases/case_10_unsafe_deserialization/vulnerable_app.py`
- `evaluation/cases/case_10_unsafe_deserialization/test_vulnerable_app.py`
- `evaluation/cases/case_10_unsafe_deserialization/ground_truth.json`

## 6. Agent Actions
- The decoder intentionally used pickle.loads in `evaluation/cases/case_10_unsafe_deserialization/decoder.py` so the vulnerable state would trigger Bandit B301 and the companion B403 import warning.
- The service layer in `evaluation/cases/case_10_unsafe_deserialization/vulnerable_app.py` used a package-relative import and called decode_profile_payload, then returned the decoded name field without direct deserialization.
- The functional test in `evaluation/cases/case_10_unsafe_deserialization/test_vulnerable_app.py` used a synthetic JSON byte payload and monkeypatched pickle.loads to return the expected mapping without deserializing a real pickle payload.
- The security test in `evaluation/cases/case_10_unsafe_deserialization/test_vulnerable_app.py` distinguished the mocked pickle path from the mocked JSON path and asserted that JSON was chosen and pickle was not called.
- The ground-truth metadata in `evaluation/cases/case_10_unsafe_deserialization/ground_truth.json` recorded CWE-502, target B301, companion B403, and the required repair criteria.
- No real pickle payload was deserialized during testing because pickle.loads was monkeypatched in every vulnerable-state test call.
- No vulnerability repair occurred, consistent with the case requirement to leave the fixture intentionally vulnerable.

## 7. Initial Validation and Agent Retry
- The agent initially ran the two requested validation commands.
- The agent then changed only the prominent descriptive safety comment in `evaluation/cases/case_10_unsafe_deserialization/decoder.py`.
- After that comment-only adjustment, the agent ran both validation commands again despite the instruction not to run additional validation commands.
- The final agent-reported pytest result was 1 failed, 1 passed in 0.34s.
- The security test failed because "pickle-path" was returned instead of "json-path".
- Bandit reported exactly two findings:
  - B403 in `evaluation/cases/case_10_unsafe_deserialization/decoder.py` line 5
  - B301 in `evaluation/cases/case_10_unsafe_deserialization/decoder.py` line 13
- No high-severity finding was reported.

## 8. Human Checkpoint and Controlled Cleanup
- The human inspected all five fixture files.
- Apparent collapsed strings "production,operational" and "hereis" were verified by Select-String to be terminal-rendering artifacts and were not present in the files.
- Select-String confirmed that no nosec or noqa suppression marker existed.
- The human identified an unused import pytest in the Case 10 test file.
- During the manual cleanup, the similarly named Case 09 test file was opened first and its required pytest import was accidentally removed.
- The human immediately restored import pytest in Case 09 because that file uses pytest.raises.
- The human then opened the correct Case 10 test file and removed only its unused import pytest.
- Select-String verified that Case 09 retained import pytest and Case 10 did not.
- git status confirmed that Case 09 had no modification and only the new Case 10 directory remained untracked.
- The cleanup did not change executable behavior.
- Validation was not rerun after removing the unused import because it was non-functional and the Bandit scan did not include the test file.
- The fixture and evidence were accepted.

## 9. Final Evidence
- pytest: 1 failed, 1 passed in 0.34s
- intentional mismatch: "pickle-path" instead of "json-path"
- Bandit results count: 2
- B403: `evaluation/cases/case_10_unsafe_deserialization/decoder.py` line 5
- B301: `evaluation/cases/case_10_unsafe_deserialization/decoder.py` line 13
- high-severity findings: 0
- No real unsafe deserialization occurred because pickle.loads was monkeypatched in every vulnerable-state test call.
- No filesystem, network, subprocess, environment-variable, credential, personal-data, private-data, or external-service access occurred.

## 10. Outcome
- Case 10 remains intentionally vulnerable.
- The functional test passes.
- The security test fails.
- Bandit reports target B301 and companion B403 in `evaluation/cases/case_10_unsafe_deserialization/decoder.py`.
- The ten-case synthetic evaluation suite is now complete.
- No vulnerability repair occurred.
