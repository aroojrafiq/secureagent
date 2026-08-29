# Build Trajectory: Ten-Case Harness Validation

## 1. Metadata
- Date: 2026-08-29
- Documentation agent: GitHub Copilot in VS Code Agent mode
- Model policy: Copilot Student Auto model selection
- Underlying automatically selected model: unknown
- Validation operator: human evaluator

## 2. Goal
The goal was to validate all ten intentionally vulnerable source fixtures together before copying them into the official expanded baseline.

## 3. Harness Scope
- 10 synthetic security cases
- 20 pytest tests total
- one functional test and one intentional security test per case
- 13 application Python files scanned by Bandit
- 8 scanner-targeted cases
- 2 intentional scanner-gap cases: Case 08 and Case 09
- 2 multi-file cases: Case 09 and Case 10
- The committed source fixtures were validated without modification.

List of the ten cases:
1. case_01_sql_injection
2. case_02_command_injection
3. case_03_hardcoded_secret
4. case_04_unsafe_eval
5. case_05_weak_hash
6. case_06_insecure_randomness
7. case_07_unsafe_archive_extraction
8. case_08_path_traversal
9. case_09_missing_authorization
10. case_10_unsafe_deserialization

## 4. Full Pytest Validation
Exact command:

.\.venv\Scripts\python.exe -m pytest evaluation/cases -q

Exact result:
- 10 failed, 10 passed in 1.30s
- All 10 functional tests passed.
- All 10 intentional security tests failed.
- The alternating result pattern was:
  .F.F.F.F.F.F.F.F.F.F

Expected security failure for each case:
- Case 01: SQL injection payload returned synthetic users instead of an empty list.
- Case 02: shell remained True instead of False.
- Case 03: the hardcoded token was returned instead of the environment token.
- Case 04: ValueError was not raised for the inert eval payload.
- Case 05: MD5 output differed from the expected SHA-256 digest.
- Case 06: "RRRRRRRR" was returned instead of "SSSSSSSS".
- Case 07: the filter keyword was absent.
- Case 08: ValueError was not raised for the traversal input.
- Case 09: PermissionError was not raised for non-owner access.
- Case 10: "pickle-path" was returned instead of "json-path".

## 5. Invalid Initial Bandit Attempt
- The first PowerShell application-file discovery used:
  Get-ChildItem evaluation\cases\case_* -Recurse -File -Filter *.py
- That wildcard form produced an empty application-file array.
- app file count was 0.
- Bandit printed its usage text and did not perform a valid scan.
- A temporary JSON result was then parsed as zero findings.
- That zero-result output was recognized as invalid immediately and is excluded from all evidence and metrics.
- No repository file was changed.

## 6. Corrected Application-File Discovery
Discovery was corrected to start from evaluation\cases and filter by directory and filename.

- Correct application-file count: 13
- Tests and __init__.py files were excluded.

Application files:
- evaluation/cases/case_01_sql_injection/vulnerable_app.py
- evaluation/cases/case_02_command_injection/vulnerable_app.py
- evaluation/cases/case_03_hardcoded_secret/vulnerable_app.py
- evaluation/cases/case_04_unsafe_eval/vulnerable_app.py
- evaluation/cases/case_05_weak_hash/vulnerable_app.py
- evaluation/cases/case_06_insecure_randomness/vulnerable_app.py
- evaluation/cases/case_07_unsafe_archive_extraction/vulnerable_app.py
- evaluation/cases/case_08_path_traversal/vulnerable_app.py
- evaluation/cases/case_09_missing_authorization/models.py
- evaluation/cases/case_09_missing_authorization/repository.py
- evaluation/cases/case_09_missing_authorization/vulnerable_app.py
- evaluation/cases/case_10_unsafe_deserialization/decoder.py
- evaluation/cases/case_10_unsafe_deserialization/vulnerable_app.py

## 7. Final Bandit Evidence
- Bandit scanned the verified 13-file array.
- JSON output was written only to the operating-system temporary directory.
- Bandit results count: 10
- Bandit exit code: 1, expected because intentionally vulnerable findings were present.
- No pytest test file was scanned.

Exact findings:

| Test ID | Severity | Repository-relative file | Line |
|---|---|---|---:|
| B608 | MEDIUM | evaluation/cases/case_01_sql_injection/vulnerable_app.py | 11 |
| B404 | LOW | evaluation/cases/case_02_command_injection/vulnerable_app.py | 7 |
| B602 | HIGH | evaluation/cases/case_02_command_injection/vulnerable_app.py | 15 |
| B105 | LOW | evaluation/cases/case_03_hardcoded_secret/vulnerable_app.py | 12 |
| B307 | MEDIUM | evaluation/cases/case_04_unsafe_eval/vulnerable_app.py | 14 |
| B324 | HIGH | evaluation/cases/case_05_weak_hash/vulnerable_app.py | 16 |
| B311 | LOW | evaluation/cases/case_06_insecure_randomness/vulnerable_app.py | 18 |
| B202 | HIGH | evaluation/cases/case_07_unsafe_archive_extraction/vulnerable_app.py | 15 |
| B403 | LOW | evaluation/cases/case_10_unsafe_deserialization/decoder.py | 5 |
| B301 | MEDIUM | evaluation/cases/case_10_unsafe_deserialization/decoder.py | 13 |

Severity totals:
- HIGH: 3
- MEDIUM: 3
- LOW: 4

- All eight scanner-targeted cases produced their required target finding.
- Case 02 also produced its expected subprocess-import companion B404.
- Case 10 also produced its expected pickle-import companion B403.
- Cases 08 and 09 produced no Bandit finding, as intentionally designed.

## 8. Output-Formatting Compatibility Note
- An attempt to format relative paths using System.IO.Path.GetRelativePath failed because the installed Windows PowerShell/.NET runtime did not provide that method.
- This did not rerun or alter the Bandit scan.
- A compatible substring-based formatter was used on the already parsed results.
- The formatter produced the exact repository-relative findings recorded above.
- This compatibility error is excluded from security metrics.

## 9. Human Checkpoint
- The human reviewed the combined pytest failure list.
- The human verified that every functional test passed and every intended security test failed.
- The human rejected the invalid empty-target Bandit attempt.
- The human verified the corrected 13-file application scope.
- The human reviewed all 10 final Bandit findings, line numbers, severities, and the two scanner-gap cases.
- git status confirmed the repository remained clean and synchronized with origin/main before documentation.
- No fixture, test, ground-truth file, dependency, or configuration was modified.
- The ten-case source harness was accepted for official expanded-baseline preparation.

## 10. Outcome
- The ten-case source harness passed its vulnerable-state integrity check.
- Exact pytest shape: 10 failed, 10 passed.
- Exact valid Bandit count: 10 findings across 13 application files.
- The suite contains both scanner-detectable and semantic reasoning cases.
- The suite contains two multi-file cases.
- Invalid diagnostic attempts are excluded from evidence and metrics.
- The harness is ready to be copied into a fresh official expanded baseline.
- No baseline repair has been run yet.
