# Build Trajectory: Official SecureAgent-Guided Hard Holdout

## 1. Metadata

- Date: 2026-08-30
- Repair agent: GitHub Copilot in VS Code Agent mode
- Model policy: Copilot Student Auto model selection
- Underlying automatically selected model: unknown
- Evaluation operator: human evaluator
- Run type: structured SecureAgent-guided hard-holdout security-repair run
- Run directory: `evaluation/runs/secureagent_official_01_hard_holdout`
- Input snapshot commit: `8a1d029`
- Protocol: `evaluation/HARD_HOLDOUT_PROTOCOL.md`

## 2. Goal

The run evaluated whether a structured scan, test, proposal, human-approval, repair, and rescan workflow could fully resolve three pre-registered hard holdouts that produced a 2-of-3 full-resolution result in the frozen generic baseline.

## 3. Frozen Input and Isolation

- The guided and generic run directories began as byte-identical copies.
- Each contained 18 Python files and no `ground_truth.json`.
- Source-to-guided mismatches: 0.
- Cross-run mismatches: 0.
- The frozen comparison input commit was `8a1d029`.
- The agent was restricted to the guided run directory.
- Public tests inside the run were visible.
- Evaluator-test source remained agent-blinded.
- The combined evaluator command could be executed, but evaluator files could not be opened.
- Bandit was permitted as part of the structured workflow.
- Source holdouts, the generic baseline, ground truth, protocol contents, traces, Git history, previous runs, and other chats were excluded.

## 4. Phase 1: Scan and Test

- The agent inspected 11 application files and 3 public tests.
- No application, test, or package file was modified.
- The only Phase 1 artifact created was `evaluation/runs/secureagent_official_01_hard_holdout/bandit-before.json`.
- Bandit scanned 11 application files.
- Pre-repair Bandit findings: 1.
- Pre-repair Bandit exit code: 1.

| Test ID | Severity | Repository-relative file | Line |
| --- | --- | --- | ---: |
| B608 | MEDIUM | `evaluation/runs/secureagent_official_01_hard_holdout/case_13/query.py` | 3 |

- Copilot's first pre-repair pytest tool invocation did not execute a usable test run.
- The invalid attempt produced no summary and modified no source file.
- The pre-registered protocol permitted a controlled rerun because no valid result existed.
- Exact valid pre-repair progress pattern: `....F.FF.FF`
- Exact valid pre-repair result: `5 failed, 6 passed in 1.01s`.
- All 3 public tests passed.
- All 3 regression tests passed.
- All 5 security tests failed for their intended rejection conditions.

## 5. Phase 1 Proposal and Human Checkpoint

- The agent identified missing authorization, URL-prefix validation bypass, and dynamic SQL sort injection.
- The agent documented legitimate behavior and regression risks and stopped before editing.
- The initial proposal mentioned supporting files that did not require changes.
- The human narrowed the approved scope to exactly three application files.
- Case 11 had to reuse `can_view_workspace`.
- Case 12 had to use parsed exact origin semantics.
- Case 13 had to use literal complete SQL branches or fixed templates without dynamic SQL-string construction.
- Suppression markers, test edits, package edits, and changes to supporting modules were prohibited.
- This checkpoint converted scanner and test evidence into a bounded repair authorization.

## 6. Approved Repair

Exactly these files were modified:

- `evaluation/runs/secureagent_official_01_hard_holdout/case_11/vulnerable_app.py`
- `evaluation/runs/secureagent_official_01_hard_holdout/case_12/vulnerable_app.py`
- `evaluation/runs/secureagent_official_01_hard_holdout/case_13/query.py`

Repairs:

- Case 11 applied the existing owner-and-collaborator policy before returning document content.
- Case 12 parsed URLs with `urllib.parse.urlsplit`, rejected user-information components, compared exact scheme and hostname, and normalized default HTTP/HTTPS ports.
- Case 13 replaced dynamic `ORDER BY` construction with literal branches for `title` and `created_at`, retained `owner_id` binding, and rejected every unsupported key.
- No dynamic SQL construction remained in the Case 13 query path.

## 7. Post-Repair Tool Failure and Human Diff Review

- Copilot attempted one post-repair pytest verification and one Bandit verification.
- Both tool outputs lacked usable summaries.
- The agent followed the protocol by stopping without retrying or editing.
- `git status --short` confirmed exactly three approved modified application files and two allowed Bandit artifacts.
- The complete three-file diff was reviewed.
- The repairs were technically correct.
- The human identified three stale comments that still described the repaired files as intentionally vulnerable.
- Only those comments were removed.
- The cleanup changed no executable behavior.
- No valid post-repair verification had occurred before that cleanup.
- The final diff was reviewed and accepted.
- CRLF-to-LF warnings were normal Git line-ending notices.

## 8. Valid Post-Repair Verification

- The invalid tool attempts were preserved in the narrative and excluded from pass/fail metrics.
- Controlled reruns were permitted because no valid result had been produced.
- Exact valid pytest progress pattern: `...........`
- Exact valid pytest result: `11 passed in 0.34s`.
- Public tests passed: 3 of 3.
- Agent-blinded regression tests passed: 3 of 3.
- Agent-blinded security tests passed: 5 of 5.
- Public test files checked: 3.
- Public test hash mismatches: 0.
- Bandit scanned 11 application Python files.
- Post-repair Bandit findings: 0.
- Post-repair Bandit exit code: 0.
- Required B608 remaining: 0.
- New high-severity findings: 0.
- Raw post-repair evidence: `evaluation/runs/secureagent_official_01_hard_holdout/bandit-after-01.json`.

## 9. Before-and-After Security Evidence

| Evidence | Before repair | After repair |
| --- | ---: | ---: |
| Pytest passed | 6 of 11 | 11 of 11 |
| Pytest failed | 5 of 11 | 0 of 11 |
| Bandit findings | 1 | 0 |
| Required B608 | Present | Removed |
| High-severity findings | 0 | 0 |

## 10. Frozen Metrics

- Cases attempted: 3
- Cases fully resolved: 3
- Full case-resolution rate: 3 of 3 (100%)
- Public tests passed: 3 of 3
- Agent-blinded regression tests passed: 3 of 3
- Agent-blinded security tests passed: 5 of 5
- Required findings before repair: 1
- Required findings after repair: 0
- Regression failures: 0
- New high-severity findings: 0
- Initial repair attempts: 1
- Repair retries after a valid verification result: 0
- Valid-command reruns caused by invalid tool execution: 3
- Unauthorized file modifications: 0

## 11. Comparison with Generic Baseline

| Metric | Generic baseline | SecureAgent-guided | Difference |
| --- | ---: | ---: | ---: |
| Fully resolved cases | 2 of 3 | 3 of 3 | +1 case |
| Full case-resolution rate | 66.7% | 100% | +33.3 percentage points |
| Post-repair tests passed | 11 of 11 | 11 of 11 | No difference |
| Required findings remaining | 1 | 0 | -1 finding |
| New high-severity findings | 0 | 0 | No difference |
| Repair retries after valid verification | 0 | 0 | No difference |

- Both approaches repaired all tested behavior.
- The generic baseline retained B608 after using allowlisted formatted SQL.
- The guided workflow removed B608 by combining initial scanning, bounded human approval, literal SQL construction, and post-repair rescanning.
- The measured difference is a verification result rather than a claim that the generic agent failed to identify all three vulnerability classes.

## 12. Artifacts

- Guided run: `evaluation/runs/secureagent_official_01_hard_holdout`
- Guided result: `evaluation/runs/secureagent_official_01_hard_holdout/RESULT.md`
- Pre-repair Bandit evidence: `evaluation/runs/secureagent_official_01_hard_holdout/bandit-before.json`
- Post-repair Bandit evidence: `evaluation/runs/secureagent_official_01_hard_holdout/bandit-after-01.json`
- Guided trajectory: `traces/build/021-secureagent-guided-hard-holdout.md`
- Generic result: `evaluation/runs/baseline_official_03_hard_holdout/RESULT.md`
- Generic trajectory: `traces/build/020-generic-hard-holdout-baseline.md`

## 13. Outcome

- The SecureAgent-guided workflow fully resolved all three hard holdouts.
- Independent validation confirmed 11 passing tests and zero Bandit findings.
- The official guided rate is 3 of 3 (100%).
- The generic baseline rate is 2 of 3 (66.7%).
- The measured improvement is one additional resolved case and 33.3 percentage points.
- The improvement came from detecting and removing a residual scanner target that behavioral tests did not expose.
- No repair retry was required after a valid verification result.
- The guided run is ready for final comparison documentation and repository integration.
