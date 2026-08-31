# SecureAgent

SecureAgent is an evidence-driven security-repair workflow for AI-generated Python code. It combines deterministic security scanning, functional and security tests, agent reasoning, bounded human approval, repair, and post-repair verification.

The project was built from scratch for the micro1 Agentic Workflows Hackathon.

## Why SecureAgent

A coding agent can produce a plausible security fix that passes behavioral tests while still leaving unresolved scanner evidence. SecureAgent makes verification and human review part of the workflow rather than treating a code edit as the finish line.

> **Key insight:** Passing functional and security tests is not always the same as satisfying an independently verified security-repair criterion.

## Headline Result

| Metric | Generic one-pass baseline | SecureAgent-guided | Difference |
| --- | ---: | ---: | ---: |
| Fully resolved hard-holdout cases | 2 of 3 | 3 of 3 | +1 case |
| Full case-resolution rate | 66.7% | 100% | +33.3 percentage points |
| Post-repair tests passed | 11 of 11 | 11 of 11 | No difference |
| Required scanner findings remaining | 1 | 0 | -1 finding |
| New high-severity findings | 0 | 0 | No difference |
| Repair retries after valid verification | 0 | 0 | No difference |

Both workflows repaired all tested runtime behavior. The generic baseline retained required Bandit finding B608 after an allowlisted formatted SQL repair. SecureAgent's scan, human-approval, and rescan workflow used literal SQL branches and removed the finding.

The measured improvement is verification completeness, not a claim that the generic agent failed to identify the vulnerability.

Link to the complete comparison:

- [Official hard-holdout comparison](evaluation/HARD_HOLDOUT_COMPARISON.md)

## Workflow

1. **Scope** - restrict the agent to an explicitly approved project or run directory.
2. **Scan** - run deterministic application-only security analysis and preserve raw evidence.
3. **Test** - execute public, regression, and security tests.
4. **Analyze** - map findings and failures to affected files, legitimate behavior, and regression risks.
5. **Approve** - stop for a human checkpoint that bounds the repair scope and requirements.
6. **Repair** - modify only approved application files.
7. **Verify** - rerun tests and security scanning with separate before-and-after evidence.
8. **Accept or retry** - accept a verified patch or authorize a bounded retry.

Invalid tool executions are documented and excluded from pass/fail metrics rather than hidden.

## Evaluation Design

The evaluation contains two complementary suites.

### Ten-Case Synthetic Harness

The first suite contains ten intentionally vulnerable Python cases covering:

- SQL injection
- command injection
- hardcoded secrets
- unsafe `eval`
- weak hashing
- insecure randomness
- unsafe archive extraction
- path traversal
- missing object-level authorization
- unsafe deserialization

The vulnerable suite produces 10 passing functional tests and 10 intentionally failing security tests. Its application-only Bandit scan produces ten findings across thirteen files.

A generic one-pass baseline repaired all ten cases behaviorally and removed every required target finding. That honest 10-of-10 ceiling result motivated the pre-registered hard-holdout comparison rather than being discarded.

### Three-Case Hard Holdout

| Case | Security challenge | Detection basis |
| --- | --- | --- |
| 11 | Multi-file collaborator authorization without blocking legitimate collaborators | Agent-blinded regression and security tests |
| 12 | URL allowlist bypass using deceptive host and user-information semantics | Agent-blinded regression and security tests |
| 13 | SQL injection through a caller-controlled dynamic sort identifier | Agent-blinded tests plus Bandit B608 |

Public tests remained inside each run. Evaluator tests were stored separately and dynamically imported the selected package through `SECUREAGENT_HOLDOUT_PACKAGE`. Ground-truth metadata was not copied into either comparison run.

The evaluator tests were agent-blinded through protocol restrictions, not claimed to be cryptographically hidden.

## Methodological Controls

- The hard-holdout protocol was pre-registered before the comparison.
- Generic and SecureAgent runs started from byte-identical 18-file Python inputs.
- Source-to-run and cross-run hash mismatches were zero.
- Both used the same public tests, evaluator tests, success criteria, and Copilot Student Auto model-selection policy.
- Neither run could modify tests or package files.
- The generic baseline received one pass without scanner access or retries.
- The guided workflow received scanning, proposal review, bounded human approval, repair, and rescanning.
- The automatically selected underlying models were unknown and may not have been identical.
- All invalid attempts and removed experiments remain documented.

## Quick Start

```powershell
git clone https://github.com/aroojrafiq/secureagent.git
Set-Location secureagent

py -3 -m venv .venv
$python = Join-Path (Resolve-Path ".").Path ".venv\Scripts\python.exe"

& $python -m pip install -r requirements-dev.txt
& $python -m pip check
```

The complete commands, expected nonzero vulnerable-state results, scanner comparisons, versions, timings, troubleshooting guidance, and safety notes are in [REPRODUCTION.md](REPRODUCTION.md).

## Clean-Reproduction Evidence

A fresh clone of commit `5d12c6e` was validated on 2026-08-31 using Python 3.13.5, pytest 9.1.1, and Bandit 1.9.4.

| Validation | Clean-clone result |
| --- | --- |
| Dependency consistency | `No broken requirements found.` |
| Repaired ten-case baseline | `20 passed` |
| Vulnerable hard-holdout suite | `5 failed, 6 passed` |
| Generic hard-holdout baseline | `11 passed`; one MEDIUM B608 remained |
| SecureAgent-guided hard holdout | `11 passed`; zero Bandit findings |

Exact runtimes vary by machine.

## Repository Map

| Path | Purpose |
| --- | --- |
| `evaluation/cases/` | Ten committed synthetic vulnerability fixtures and ground truth |
| `evaluation/holdout_cases/` | Three pre-registered hard-holdout source fixtures |
| `evaluation/evaluator_tests/hard_holdout/` | Agent-blinded regression and security tests |
| `evaluation/runs/` | Frozen inputs, repaired outputs, result summaries, and raw scanner evidence |
| `evaluation/HARD_HOLDOUT_PROTOCOL.md` | Pre-registered comparison protocol |
| `evaluation/HARD_HOLDOUT_COMPARISON.md` | Final generic-versus-guided comparison |
| `traces/build/` | Chronological build and evaluation trajectories |
| `IMPROVEMENT_CHANGELOG.md` | Baselines, revised experiments, final decisions, and lessons |
| `REPRODUCTION.md` | Clean setup and exact reproduction commands |

## Evidence

- [Final hard-holdout comparison](evaluation/HARD_HOLDOUT_COMPARISON.md)
- [Pre-registered hard-holdout protocol](evaluation/HARD_HOLDOUT_PROTOCOL.md)
- [Generic hard-holdout result](evaluation/runs/baseline_official_03_hard_holdout/RESULT.md)
- [SecureAgent-guided result](evaluation/runs/secureagent_official_01_hard_holdout/RESULT.md)
- [Generic Bandit evidence](evaluation/runs/baseline_official_03_hard_holdout/bandit-results.json)
- [Guided pre-repair Bandit evidence](evaluation/runs/secureagent_official_01_hard_holdout/bandit-before.json)
- [Guided post-repair Bandit evidence](evaluation/runs/secureagent_official_01_hard_holdout/bandit-after-01.json)
- [Improvement changelog](IMPROVEMENT_CHANGELOG.md)
- [Reproduction guide](REPRODUCTION.md)
- [Build trajectories](traces/build)

## Limitations

- The hard holdout contains only three synthetic cases.
- Each workflow was run once; the comparison is not statistically significant.
- Copilot Student Auto did not expose the underlying selected model.
- Evaluator blinding relied on protocol restrictions rather than cryptographic isolation.
- Scanner access was intentionally available only to the guided workflow because that workflow difference was the intervention.
- The generic residual B608 may reflect scanner conservatism after an allowlist rather than a demonstrably exploitable runtime flaw.
- Synthetic fixtures do not directly establish performance on large production repositories.
- Three guided-run command reruns were required because Copilot tool output was invalid; these were operational reruns, not repair retries.

## Safety

All vulnerability fixtures are synthetic and intentionally insecure. They must never be reused in production. The project uses synthetic identities, tokens, payloads, URLs, reports, and database records and does not require real credentials, production data, private data, or external-service access.

## Status

The core workflow, ten-case evaluation, pre-registered hard-holdout comparison, raw evidence, improvement changelog, and clean-environment reproduction have been completed. Final submission and demonstration preparation are in progress.

## License

See [LICENSE](LICENSE).
