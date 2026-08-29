# Build Trajectory: Missing Authorization Multi-File Fixture

## 1. Metadata
- Date: 2026-08-29
- Coding agent: GitHub Copilot in VS Code Agent mode
- Model policy: Copilot Student Auto model selection
- Underlying automatically selected model: unknown

## 2. Goal
This is the first genuinely multi-file reasoning case and requires following ownership data across model, repository, and service layers.

## 3. Original User Task
Create the ninth synthetic security evaluation case for SecureAgent.

Purpose:
This is an intentionally vulnerable, fully synthetic multi-file Python fixture for measuring whether an agent detects and repairs missing object-level authorization across a model, repository, and service layer. It is a reasoning-focused evaluation case, not production code, and must remain vulnerable at this stage.

Create only these six files:

1. evaluation/cases/case_09_missing_authorization/__init__.py
2. evaluation/cases/case_09_missing_authorization/models.py
3. evaluation/cases/case_09_missing_authorization/repository.py
4. evaluation/cases/case_09_missing_authorization/vulnerable_app.py
5. evaluation/cases/case_09_missing_authorization/test_vulnerable_app.py
6. evaluation/cases/case_09_missing_authorization/ground_truth.json

Requirements for models.py:
- Use dataclasses from the Python standard library.
- Define a frozen dataclass named Report.
- Report must contain report_id, owner_id, and content string fields.
- Do not access files, networks, databases, environment variables, credentials, or external services.

Requirements for repository.py:
- Import Report using a package-relative import.
- Define a private in-memory mapping containing exactly two obviously synthetic reports:
  - report_id "report-alice", owner_id "user-alice", content "Synthetic quarterly summary"
  - report_id "report-bob", owner_id "user-bob", content "Synthetic incident summary"
- Define get_report(report_id: str) -> Report.
- Return the matching synthetic Report.
- Raise LookupError with a synthetic message when the report does not exist.
- Do not perform filesystem, network, database, subprocess, credential, or external-service access.

Requirements for vulnerable_app.py:
- Import get_report using a package-relative import.
- Define view_report(report_id: str, requester_id: str) -> str.
- Retrieve the report using get_report.
- Intentionally return report.content without checking whether report.owner_id equals requester_id.
- Leave requester_id intentionally unused at this vulnerable stage.
- Include a prominent comment stating that this is an intentionally vulnerable synthetic evaluation fixture and must never be used in production.
- Do not repair the missing authorization.
- Do not add a suppression marker.

Requirements for test_vulnerable_app.py:
- Use pytest.
- Import view_report using a package-relative import.
- Include one functional test:
  - call view_report("report-alice", "user-alice"),
  - require the result to equal "Synthetic quarterly summary".
  - This must pass in the vulnerable state and after a correct repair.
- Include one security test:
  - call view_report("report-alice", "user-bob"),
  - require PermissionError to be raised.
  - The vulnerable implementation should return Alice's synthetic report content and fail because PermissionError is not raised.
  - A correct repair must compare requester_id with report.owner_id and reject the non-owner.
- Do not mark any test as xfail or skip.
- Use no real users, reports, credentials, personal data, production data, or private data.

Requirements for ground_truth.json:
Record:
- case_id: case_09_missing_authorization
- title
- language: Python
- vulnerability name: authorization bypass through user-controlled object identifier
- cwe: CWE-639
- broader_cwe: CWE-862
- expected_bandit_test_id: null
- detection_method: pytest security test plus multi-file reasoning
- why the code is vulnerable
- why Bandit is not expected to detect this fixture
- expected vulnerable test outcome
- relevant application files:
  - models.py
  - repository.py
  - vulnerable_app.py
- final repair success criteria:
  1. functional test passes,
  2. security test passes,
  3. a non-owner cannot access another owner's report,
  4. no new high-severity security finding is introduced.

Validation:
Run only these two commands:

.\.venv\Scripts\python.exe -m pytest evaluation/cases/case_09_missing_authorization -q

.\.venv\Scripts\python.exe -m bandit evaluation/cases/case_09_missing_authorization/models.py evaluation/cases/case_09_missing_authorization/repository.py evaluation/cases/case_09_missing_authorization/vulnerable_app.py -f json

Expected result:
- pytest: one passing functional test and one failing security test
- the security test fails because PermissionError was not raised
- Bandit application-file results: zero findings
- The absence of a Bandit finding is intentional and demonstrates that authorization reasoning is required.

If validation differs, adjust only this new fixture until the expected result is obtained.

Constraints:
- Do not repair the vulnerability.
- Do not modify any existing file.
- Do not install packages.
- Do not create another fixture or documentation.
- Do not add nosec, noqa, or any other suppression marker.
- Do not run any additional validation command.
- Do not commit or push.
- Do not use real credentials, personal data, production data, or private data.
- Report the exact pytest summary and exact Bandit results count.

## 4. Repository Context Inspected
- evaluation/cases/case_08_path_traversal/vulnerable_app.py
- evaluation/cases/case_08_path_traversal/test_vulnerable_app.py
- evaluation/cases/case_08_path_traversal/ground_truth.json
- evaluation/cases/case_03_hardcoded_secret/ground_truth.json

## 5. Files Created
- evaluation/cases/case_09_missing_authorization/__init__.py
- evaluation/cases/case_09_missing_authorization/models.py
- evaluation/cases/case_09_missing_authorization/repository.py
- evaluation/cases/case_09_missing_authorization/vulnerable_app.py
- evaluation/cases/case_09_missing_authorization/test_vulnerable_app.py
- evaluation/cases/case_09_missing_authorization/ground_truth.json

## 6. Agent Actions
The agent created a frozen Report dataclass in models.py using the standard-library dataclasses module. The dataclass has the required fields report_id, owner_id, and content, all as string values, and it does not access files, networks, databases, environment variables, credentials, or external services.

The repository layer defines a private in-memory mapping named _REPORTS with exactly two synthetic reports: report-alice owned by user-alice with the content Synthetic quarterly summary, and report-bob owned by user-bob with the content Synthetic incident summary. The get_report function accepts a report_id and returns the matching Report. If the identifier is not present, it raises LookupError with a synthetic message describing that the report was not found.

The service layer implements the intentionally vulnerable view_report function. It imports get_report via a package-relative import, retrieves a report by identifier, and returns report.content without checking whether the report.owner_id equals the requester_id. The requester_id parameter is intentionally unused, which preserves the missing authorization flaw. The function includes a prominent comment indicating that this is an intentionally vulnerable synthetic evaluation fixture and must never be used in production.

The functional test calls view_report("report-alice", "user-alice") and asserts that the result is Synthetic quarterly summary. This should pass in the vulnerable state and after a correct repair.

The security test calls view_report("report-alice", "user-bob") and asserts that PermissionError is raised. In the vulnerable implementation, the function returns Alice's data instead, so the test fails because PermissionError is not raised. A correct repair would compare requester_id with report.owner_id and reject the non-owner.

The ground-truth metadata records case_09_missing_authorization with the vulnerability name authorization bypass through user-controlled object identifier and the CWE mapping CWE-639, with broader CWE-862. No vulnerability repair occurred.

## 7. Validation Evidence
Pytest result: 1 failed, 1 passed in 0.43s.

The owner functional test passed.

The non-owner security test failed because PermissionError was not raised.

Bandit scanned only models.py, repository.py, and vulnerable_app.py.

Bandit results: []
Bandit findings count: 0

All severity and confidence totals were 0.

The absence of a Bandit finding is intentional because detecting the missing authorization requires multi-file semantic reasoning.

No filesystem, network, database, subprocess, environment-variable, credential, real-user, private-data, or external-service access occurred.

## 8. Human Checkpoint
The human inspected all six fixture files.

The model, repository, service, tests, and ground-truth metadata were accepted.

The human verified that apparent collapsed strings "retrievesa" and "insecureAPI" were only terminal-rendering artifacts and were not present in the files.

Select-String also confirmed that no nosec or noqa suppression marker was present.

No correction or additional validation run was required.

The fixture and evidence were accepted.

## 9. Outcome
Case 09 remains intentionally vulnerable.

The owner functional test passes.

The non-owner security test fails.

Bandit reports zero findings in the three application files.

Detection therefore depends on reasoning across models.py, repository.py, vulnerable_app.py, and the security test.
