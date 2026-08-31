# Build Trajectory: Clean-Environment Reproduction

## 1. Metadata

- Date: 2026-08-31
- Reproduction operator: human evaluator
- Documentation agent: GitHub Copilot in VS Code Agent mode
- Source repository: `https://github.com/aroojrafiq/secureagent.git`
- Reproduced commit: `5d12c6e`
- Operating system: Windows
- Python: 3.13.5
- pip: 25.1.1
- pytest: 9.1.1
- Bandit: 1.9.4

## 2. Goal

The goal was to test whether a new user could clone the committed repository into a fresh directory, create an independent virtual environment, install only declared dependencies, and reproduce the project's principal pytest and Bandit results without relying on the development workspace.

## 3. Clean Setup

- The working repository was clean and synchronized with `origin/main`.
- A uniquely named clone was created under the operating-system temporary directory.
- The clean clone resolved to commit `5d12c6e`.
- The clean clone initially had no tracked or untracked changes.
- A separate `.venv` was created inside the temporary clone with the system Python launcher.
- Dependencies were installed only from `requirements-dev.txt`.
- pip installed the pinned `bandit==1.9.4` and `pytest==9.1.1` requirements and their dependencies.
- `python -m pip check` reported `No broken requirements found.`
- Upgrading pip was not required.
- The temporary clone remained clean after dependency installation and validation.

## 4. Hard-Holdout Pytest Reproduction

| Run | Progress or result | Exit code | Clean runtime |
| --- | --- | ---: | ---: |
| Vulnerable source harness | `....F.FF.FF`; 5 failed, 6 passed | 1 | 1.91s |
| Generic hard-holdout baseline | 11 passed | 0 | 0.87s |
| SecureAgent-guided hard holdout | 11 passed | 0 | 0.56s |

- The vulnerable source reproduced all 3 passing public tests, all 3 passing regression tests, and all 5 intentional security failures.
- The generic and guided repaired runs both reproduced 11 passing tests.

## 5. Hard-Holdout Bandit Reproduction

| Run | Application files | Findings | Detail | Exit code |
| --- | ---: | ---: | --- | ---: |
| Generic hard-holdout baseline | 11 | 1 | B608, MEDIUM, Case 13 `query.py`, line 13 | 1 |
| SecureAgent-guided hard holdout | 11 | 0 | No findings | 0 |

The clean clone reproduced the exact scanner distinction used by the final comparison.

## 6. Ten-Case Pytest Reproduction

| Run | Progress or result | Exit code | Clean runtime |
| --- | --- | ---: | ---: |
| Vulnerable ten-case source | `.F.F.F.F.F.F.F.F.F.F`; 10 failed, 10 passed | 1 | 2.03s |
| Repaired official ten-case baseline | 20 passed | 0 | 1.24s |

Every functional test passed in the vulnerable source suite, while all ten security tests failed intentionally.

## 7. Ten-Case Bandit Reproduction

| Run | Application files | Findings | Severity summary | Exit code |
| --- | ---: | ---: | --- | ---: |
| Vulnerable ten-case source | 13 | 10 | 3 HIGH, 3 MEDIUM, 4 LOW | 1 |
| Repaired official ten-case baseline | 13 | 3 | 3 LOW | 1 |

- The vulnerable source reproduced B608, B404, B602, B105, B307, B324, B311, B202, B403, and B301.
- The repaired baseline retained only B404, B607, and B603 in Case 02.
- All required target findings were removed from the repaired ten-case baseline.
- No HIGH finding remained.

## 8. Documentation Gap Discovered

- The clean clone revealed that `REPRODUCTION.md` still contained placeholders for prerequisites, setup, commands, expected output, versions, runtime, and cost.
- `README.md` still described the implemented workflow as planned and the repository status as initial hackathon development.
- These stale documents materially weakened reproducibility and judge-facing clarity despite the underlying evidence being complete.
- No application, test, protocol, result, scanner JSON, dependency, or evaluation file required correction.

## 9. Documentation Corrections

Only these existing files were changed:

- `README.md`
- `REPRODUCTION.md`

`REPRODUCTION.md` now contains:

- validated Windows clean-setup instructions,
- exact pytest commands,
- exact application-only Bandit discovery and scan commands,
- expected exit-code interpretation,
- clean-reproduction versions and timings,
- evidence links,
- runtime and cost disclosures,
- safety notes,
- troubleshooting guidance.

`README.md` now contains:

- the completed workflow,
- the 2-of-3 versus 3-of-3 headline comparison,
- the 33.3-percentage-point measured improvement,
- the ten-case and hard-holdout evaluation design,
- methodological controls,
- clean-reproduction evidence,
- repository structure,
- limitations,
- safety and status information,
- direct links to committed evidence.

No unsupported compatibility, cost, or security claim was added.

## 10. Human Checkpoint

- The human executed every clean-reproduction validation command.
- Expected nonzero vulnerable-state and Bandit exit codes were interpreted from their textual summaries rather than treated as setup failures.
- Scanner JSON created during reproduction was written only to the operating-system temporary directory.
- Apparent collapsed strings in terminal output were checked with `Select-String` and confirmed to be rendering artifacts.
- Unicode punctuation that displayed poorly in Windows PowerShell was normalized where necessary.
- Both the temporary clone and working repository were confirmed clean before documentation changes.
- The README and reproduction guide were inspected before acceptance.

## 11. Final Evidence

- Fresh clone: successful
- Fresh virtual environment: successful
- Declared dependency installation: successful
- Broken requirements: 0
- Vulnerable ten-case shape reproduced: yes
- Repaired ten-case result reproduced: yes
- Vulnerable hard-holdout shape reproduced: yes
- Generic hard-holdout result reproduced: yes
- SecureAgent-guided result reproduced: yes
- Generic residual B608 reproduced: yes
- Guided zero-finding scan reproduced: yes
- Unexpected repository modifications during validation: 0

## 12. Outcome

The repository's principal evaluation results were independently reproduced from a clean clone using only the declared dependencies. The exercise exposed and corrected stale top-level documentation rather than a code or evidence defect. SecureAgent now has an evidence-backed README and a complete clean-environment reproduction guide suitable for final validation and demonstration preparation.
