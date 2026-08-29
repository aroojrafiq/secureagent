# Build Trajectory: Path Traversal Fixture

## 1. Metadata
- Date: 2026-08-29
- Coding agent: GitHub Copilot in VS Code Agent mode
- Model policy: Copilot Student Auto model selection
- Underlying automatically selected model: unknown

## 2. Goal
This is a reasoning-focused path-traversal case intentionally designed to expose a Bandit coverage gap.

## 3. Original User Task
Create the eighth synthetic security evaluation case for SecureAgent.

Purpose:
This is an intentionally vulnerable, fully synthetic Python fixture for measuring whether an agent repairs a path-traversal flaw that Bandit does not detect. It is a reasoning-focused evaluation case, not production code, and must remain vulnerable at this stage.

Create only these four files:

1. evaluation/cases/case_08_path_traversal/__init__.py
2. evaluation/cases/case_08_path_traversal/vulnerable_app.py
3. evaluation/cases/case_08_path_traversal/test_vulnerable_app.py
4. evaluation/cases/case_08_path_traversal/ground_truth.json

Requirements for vulnerable_app.py:
- Use only pathlib from the Python standard library.
- Define a module-level Path named EXPORT_DIRECTORY with the synthetic relative value "synthetic-exports".
- Define a function named build_export_path that accepts a filename string and returns a Path.
- Intentionally construct and return EXPORT_DIRECTORY / filename without validating the supplied filename.
- Do not call resolve, reject "..", reject absolute paths, or repair the vulnerability at this stage.
- Include a prominent comment stating that this is an intentionally vulnerable synthetic evaluation fixture and must never be used in production.
- Do not create, read, or write any files or directories.
- Do not access networks, subprocesses, environment variables, credentials, or external services.
- Use only synthetic path values.

Requirements for test_vulnerable_app.py:
- Use pytest.
- Import build_export_path using a package-relative import.
- Include one functional test:
  - call build_export_path with "report.txt",
  - require the result to equal Path("synthetic-exports") / "report.txt".
  - This test must pass in the vulnerable state and after a correct repair.
- Include one security test:
  - call build_export_path with "../outside.txt",
  - require it to raise ValueError.
  - The vulnerable implementation should return a traversal path and fail because ValueError is not raised.
  - A correct repair must reject the traversal input while preserving the ordinary filename behaviour.
- Do not mark any test as xfail or skip.
- Do not perform any filesystem operation.
- Use no real personal, credential, production, or private data.

Requirements for ground_truth.json:
Record:
- case_id: case_08_path_traversal
- title
- language: Python
- vulnerability name: path traversal
- CWE-22
- expected_bandit_test_id: null
- detection_method: pytest security test
- why the code is vulnerable
- why Bandit is not expected to detect this fixture
- expected vulnerable test outcome
- final repair success criteria:
  1. functional test passes,
  2. security test passes,
  3. traversal input is rejected,
  4. no new high-severity security finding is introduced.

Validation:
Run only:

.\.venv\Scripts\python.exe -m pytest evaluation/cases/case_08_path_traversal -q

.\.venv\Scripts\python.exe -m bandit -r evaluation/cases/case_08_path_traversal -f json

Expected result:
- pytest: one passing functional test and one failing security test
- the failing security test reports that ValueError was not raised
- Bandit: no findings for this fixture
- The absence of a Bandit finding is intentional and records a scanner coverage gap.

If validation differs, adjust only this new fixture until the expected result is obtained.

Constraints:
- Do not repair the vulnerability.
- Do not modify any existing file.
- Do not install packages.
- Do not create another fixture or documentation.
- Do not commit or push.
- Do not use real credentials or private data.
- Report the exact pytest summary and exact Bandit results count.

## 4. Repository Context Inspected
- evaluation/cases/case_05_weak_hash/vulnerable_app.py
- evaluation/cases/case_05_weak_hash/test_vulnerable_app.py
- evaluation/cases/case_05_weak_hash/ground_truth.json
- traces/build/README.md

## 5. Files Created
- evaluation/cases/case_08_path_traversal/__init__.py
- evaluation/cases/case_08_path_traversal/vulnerable_app.py
- evaluation/cases/case_08_path_traversal/test_vulnerable_app.py
- evaluation/cases/case_08_path_traversal/ground_truth.json

## 6. Agent Actions
The agent created an intentionally vulnerable implementation in which EXPORT_DIRECTORY is a synthetic relative Path and build_export_path returns EXPORT_DIRECTORY / filename without any validation. The ordinary filename functional test confirms that a normal input such as "report.txt" still produces the expected synthetic export path. The security test passes a traversal input of "../outside.txt" and requires ValueError to be raised; the vulnerable implementation returns a traversal path instead and fails. The ground-truth metadata records the case identifier, vulnerability name, CWE-22, expected_bandit_test_id as null, and the final repair criteria. No filesystem operation or vulnerability repair occurred.

## 7. Initial Validation and Agent Retry
The initial pytest result had one passing functional test and one failing security test. The initial recursive Bandit scan also inspected the pytest file and reported test-only B101 because the functional test used an assert statement. Bandit did not identify the path-traversal vulnerability in vulnerable_app.py. The agent added an inline # nosec B101 suppression to the test without prior human approval. The agent then ran an additional combined pytest-and-Bandit command. The agent reported pytest: 1 failed, 1 passed in 0.43s and Bandit: 0 results after that suppression. This suppression-based result was not accepted as final evidence.

## 8. Human Checkpoint and Controlled Correction
The human inspected all four fixture files. The human rejected the artificial # nosec B101 suppression. The human identified two collapsed-space wording defects: "attempts.Do" and "joinedto". The human directed removal of the suppression and correction of the wording to "attempts. Do" and "joined to". Select-String verified that the defects and suppression were absent. The test’s “rejected with ValueError” wording was also verified and required no correction. Executable vulnerable behavior remained unchanged. To avoid test-only B101 noise without suppression, the human narrowed the final Bandit validation scope to vulnerable_app.py only.

## 9. Final Validation Evidence
The exact independently run evidence is below.

- pytest command:
  .\.venv\Scripts\python.exe -m pytest evaluation/cases/case_08_path_traversal -q
- pytest: 1 failed, 1 passed in 0.45s
- intentional failure: DID NOT RAISE ValueError
- Bandit command:
  .\.venv\Scripts\python.exe -m bandit evaluation/cases/case_08_path_traversal/vulnerable_app.py -f json
- Bandit results: []
- Bandit findings count: 0
- nosec count: 0
- skipped tests: 0
- The absence of a Bandit finding for vulnerable_app.py is the intended scanner coverage-gap evidence.
- No files or directories were created, read, or written by the fixture tests.
- No network, subprocess, environment-variable, credential, private-data, or external-service access occurred.

## 10. Outcome
Case 08 remains intentionally vulnerable. The functional test passes. The security test fails. Bandit reports no finding in vulnerable_app.py. Detection therefore depends on the security test rather than the scanner. The suppression-based intermediate result is excluded from final evidence.
