# Official SecureAgent-Guided Hard-Holdout Result

## 1. Metadata

- Date: 2026-08-30
- Run directory: `evaluation/runs/secureagent_official_01_hard_holdout`
- Input snapshot commit: `8a1d029`
- Repair agent: GitHub Copilot in VS Code Agent mode
- Model policy: Copilot Student Auto model selection
- Underlying automatically selected model: unknown
- Evaluation operator: human evaluator
- Run type: structured SecureAgent-guided hard-holdout security-repair run
- Protocol: `evaluation/HARD_HOLDOUT_PROTOCOL.md`

## 2. Protocol and Isolation

- The guided run received a byte-identical Python copy of the same three hard holdouts used by the generic baseline.
- The input contained 18 Python files and no `ground_truth.json` files.
- Source-to-guided and cross-run hash mismatches were 0 before repair.
- The agent was restricted to `evaluation/runs/secureagent_official_01_hard_holdout`.
- The agent could inspect application files and public tests in its run.
- Evaluator-test source remained agent-blinded.
- The agent could execute the combined evaluator command and observe failure output without opening evaluator files.
- The agent could use Bandit as part of the scan-and-verify workflow.
- The workflow used scan and test, analysis and proposal, human approval, repair, verification, and human acceptance.
- The protocol allowed one initial repair attempt and at most two repair retries.
- No source holdout, generic baseline, ground truth, protocol, trace, Git history, previous run, or other chat was inspected.

## 3. Phase 1 Scan and Test Evidence

- Bandit scanned 11 application Python files.
- Public tests and `__init__.py` files were excluded.
- Raw pre-repair evidence: `evaluation/runs/secureagent_official_01_hard_holdout/bandit-before.json`
- Pre-repair Bandit findings: 1
- Pre-repair Bandit exit code: 1
- Finding:

| Test ID | Severity | Repository-relative file | Line |
| --- | --- | --- | ---: |
| B608 | MEDIUM | `evaluation/runs/secureagent_official_01_hard_holdout/case_13/query.py` | 3 |

- The first Copilot pre-repair pytest tool invocation produced no executed-test summary and was invalid.
- No source file was modified by that invalid attempt.
- The protocol-permitted controlled evaluator rerun produced the valid evidence below.
- Exact pre-repair progress pattern: `....F.FF.FF`
- Exact pre-repair summary: `5 failed, 6 passed in 1.01s`
- All 3 public tests passed.
- All 3 regression tests passed.
- All 5 security tests failed.
- Case 11 did not raise `PermissionError` for outsider access.
- Case 12 did not raise `ValueError` for the deceptive-host or user-information-confusion URLs.
- Case 13 did not raise `ValueError` for the injected expression or unsupported modifier.
- Both Case 13 security tests confirmed that all four synthetic rows remained intact.

## 4. Human Repair Approval

- The agent proposed repairs and stopped before editing.
- The human reviewed the scan evidence, test failures, legitimate behavior, and regression risks.
- The human narrowed the approved scope to exactly three application files.
- Case 11 approval required reuse of the existing owner-and-collaborator policy.
- Case 12 approval required parsed exact scheme, hostname, and port semantics.
- Case 13 approval required fixed complete SQL templates or literal branches without dynamic SQL-string construction.
- Tests, package files, supporting modules, and the pre-repair evidence artifact were not authorized for modification.

## 5. Repair Scope

Exactly these three application files were modified:

- `evaluation/runs/secureagent_official_01_hard_holdout/case_11/vulnerable_app.py`
- `evaluation/runs/secureagent_official_01_hard_holdout/case_12/vulnerable_app.py`
- `evaluation/runs/secureagent_official_01_hard_holdout/case_13/query.py`

Repairs:

- Case 11 imported and applied `can_view_workspace`, preserving owner and collaborator access and raising `PermissionError` for outsiders.
- Case 12 used `urllib.parse.urlsplit`, rejected user-information components, compared exact scheme and hostname, and normalized default HTTP/HTTPS ports before comparison.
- Case 13 used literal SQL branches for `title` and `created_at`, retained the bound `owner_id` parameter, and raised `ValueError` for every unsupported key.
- No dynamic SQL construction remained in the Case 13 query path.
- During human diff review, the three now-inaccurate intentionally-vulnerable comments were removed.
- That comment-only cleanup changed no executable behavior.
- No test, `__init__.py`, model, policy, repository, configuration, transport, dependency, or unrelated file was modified.

## 6. Post-Repair Verification

- Copilot attempted one post-repair pytest command and one Bandit command, but their tool output contained no usable summaries.
- The agent correctly stopped without retrying or editing.
- The human reviewed the complete diff before accepting it.
- Because the tool attempts produced no valid verification result, controlled reruns were permitted.
- Exact valid post-repair progress pattern: `...........`
- Exact valid post-repair pytest result: `11 passed in 0.34s`
- Public tests passed: 3 of 3.
- Agent-blinded regression tests passed: 3 of 3.
- Agent-blinded security tests passed: 5 of 5.
- Public test files checked: 3.
- Public test hash mismatches: 0.
- Post-repair Bandit application files scanned: 11.
- Raw post-repair evidence: `evaluation/runs/secureagent_official_01_hard_holdout/bandit-after-01.json`
- Post-repair Bandit findings: 0.
- Post-repair Bandit exit code: 0.
- Required B608 remaining: 0.
- New high-severity findings: 0.

## 7. Per-Case Outcome

| Case | Public behavior | Regression behavior | Security behavior | Bandit | Outcome |
| --- | --- | --- | --- | --- | --- |
| Case 11 | Passed | Collaborator access passed | Outsider rejection passed | No finding expected | Resolved |
| Case 12 | Passed | Allowed-origin request passed | Both bypass rejections passed | No finding expected | Resolved |
| Case 13 | Passed | `created_at` sorting passed | Both unsafe sort inputs were rejected | B608 removed | Resolved |

## 8. Frozen Metrics

- Cases attempted: 3
- Cases fully resolved: 3
- Full case-resolution rate: 3 of 3 (100%)
- Behaviorally repaired cases: 3 of 3
- Public tests passed: 3 of 3
- Agent-blinded regression tests passed: 3 of 3
- Agent-blinded security tests passed: 5 of 5
- Total tests passed: 11 of 11
- Required findings before repair: 1
- Required findings after repair: 0
- New high-severity findings: 0
- Regression failures: 0
- Initial repair attempts: 1
- Repair retries after a valid verification result: 0
- Valid-command reruns caused by invalid tool execution: 3
- Unauthorized file modifications: 0

## 9. Comparison with the Frozen Generic Baseline

| Metric | Generic baseline | SecureAgent-guided | Difference |
| --- | ---: | ---: | ---: |
| Fully resolved cases | 2 of 3 | 3 of 3 | +1 case |
| Full case-resolution rate | 66.7% | 100% | +33.3 percentage points |
| Post-repair tests passed | 11 of 11 | 11 of 11 | No difference |
| Required findings remaining | 1 | 0 | -1 finding |
| New high-severity findings | 0 | 0 | No difference |
| Repair retries after valid verification | 0 | 0 | No difference |

- Both approaches repaired all tested behavior.
- The difference appeared only during independent security scanning.
- The generic baseline retained B608 after using allowlisted formatted SQL.
- The guided workflow's pre-repair scan, human-approved fixed-query requirement, and post-repair rescan removed B608.
- The comparison demonstrates a verification improvement, not a claim that the generic agent failed to understand all three vulnerabilities.

## 10. Artifacts

- Repaired guided run: `evaluation/runs/secureagent_official_01_hard_holdout`
- Pre-repair Bandit evidence: `evaluation/runs/secureagent_official_01_hard_holdout/bandit-before.json`
- Post-repair Bandit evidence: `evaluation/runs/secureagent_official_01_hard_holdout/bandit-after-01.json`
- Result summary: `evaluation/runs/secureagent_official_01_hard_holdout/RESULT.md`
- Generic baseline result: `evaluation/runs/baseline_official_03_hard_holdout/RESULT.md`

## 11. Outcome

- The SecureAgent-guided workflow fully resolved all three hard-holdout cases.
- Independent evidence confirmed 11 passing tests and zero Bandit findings.
- The official guided resolution rate is 3 of 3 (100%).
- The frozen generic baseline resolution rate is 2 of 3 (66.7%).
- The measured improvement is one additional fully resolved case and 33.3 percentage points.
- The improvement came from verification and rescan evidence identifying a residual target that behavioral tests alone did not expose.
- No repair retry was required after a valid verification result.
- The result is ready for final trajectory documentation and comparison reporting.
