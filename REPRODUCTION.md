# Reproducing SecureAgent Evaluations

## 1. Purpose

SecureAgent is an evidence-driven security-repair workflow for AI-generated Python code. This guide reproduces the committed synthetic source-harness behavior, the frozen generic baselines, and the official SecureAgent-guided hard-holdout result.

Some source-harness commands intentionally return nonzero exit codes because vulnerable-state security tests and scanner findings are expected. Expected nonzero results are evidence, not setup failures.

## 2. Prerequisites

- Git
- Python 3.13
- Internet access for the initial dependency installation
- PowerShell for the exact Windows commands below

The clean reproduction was validated with:

- Windows
- Python 3.13.5
- pip 25.1.1
- pytest 9.1.1
- Bandit 1.9.4
- Repository commit `5d12c6e`

The repository declares its development dependencies in `requirements-dev.txt`.

## 3. Clean Windows Setup

```powershell
git clone https://github.com/aroojrafiq/secureagent.git
Set-Location secureagent

py -3 -m venv .venv
$python = Join-Path (Resolve-Path ".").Path ".venv\Scripts\python.exe"

& $python -m pip install -r requirements-dev.txt
& $python -m pip check
```

Expected dependency check:

```
No broken requirements found.
```

Upgrading pip is not required.

## 4. Reproduce the Vulnerable Hard-Holdout Source

```powershell
$env:SECUREAGENT_HOLDOUT_PACKAGE = "evaluation.holdout_cases"
& $python -m pytest evaluation/holdout_cases evaluation/evaluator_tests/hard_holdout -q
```

Expected vulnerable-state result:

- Progress pattern: `....F.FF.FF`
- `5 failed, 6 passed`
- Exit code: 1
- All 3 public tests pass.
- All 3 legitimate regression tests pass.
- All 5 security tests fail intentionally.
- Case 11 does not reject outsider access.
- Case 12 does not reject two deceptive URLs.
- Case 13 does not reject two unsafe sort expressions.

Exact runtime varies by machine. The clean reproduction on 2026-08-31 completed in 1.91 seconds.

## 5. Reproduce the Generic Hard-Holdout Baseline

```powershell
$env:SECUREAGENT_HOLDOUT_PACKAGE = "evaluation.runs.baseline_official_03_hard_holdout"
& $python -m pytest evaluation/runs/baseline_official_03_hard_holdout evaluation/evaluator_tests/hard_holdout -q
```

Expected result:

- `11 passed`
- Exit code: 0
- Clean-reproduction runtime: 0.87 seconds

Behavioral tests all pass. The frozen full-resolution criterion also requires removal of the required Bandit target.

## 6. Reproduce the SecureAgent-Guided Hard-Holdout Result

```powershell
$env:SECUREAGENT_HOLDOUT_PACKAGE = "evaluation.runs.secureagent_official_01_hard_holdout"
& $python -m pytest evaluation/runs/secureagent_official_01_hard_holdout evaluation/evaluator_tests/hard_holdout -q
```

Expected result:

- `11 passed`
- Exit code: 0
- Clean-reproduction runtime: 0.56 seconds

## 7. Reproduce the Hard-Holdout Scanner Difference

```powershell
$scanRoots = [ordered]@{
    "generic baseline" = "evaluation\runs\baseline_official_03_hard_holdout"
    "SecureAgent-guided" = "evaluation\runs\secureagent_official_01_hard_holdout"
}

foreach ($entry in $scanRoots.GetEnumerator()) {
    $appFiles = Get-ChildItem $entry.Value -Recurse -File -Filter *.py |
        Where-Object {
            $_.Directory.Name -like "case_*" -and
            $_.Name -notin @("__init__.py", "test_public_behavior.py")
        } |
        ForEach-Object { $_.FullName }

    $safeName = $entry.Key.Replace(" ", "-")
    $outputPath = Join-Path $env:TEMP "secureagent-$safeName-bandit.json"

    & $python -m bandit -f json -o $outputPath @appFiles
    $scanExit = $LASTEXITCODE
    $scanResults = (Get-Content $outputPath -Raw | ConvertFrom-Json).results
    $repoRoot = (Resolve-Path ".").Path

    "`n$($entry.Key):"

    $scanResults | ForEach-Object {
        $relativePath = $_.filename.Substring($repoRoot.Length + 1)
        "$($_.test_id) | $($_.issue_severity) | $relativePath | line $($_.line_number)"
    }

    "application files scanned: $($appFiles.Count)"
    "results count: $($scanResults.Count)"
    "Bandit exit code: $scanExit"
}
```

Expected scanner results:

| Run | Files scanned | Findings | Expected detail | Exit code |
|-----|---|---|---|---|
| Generic baseline | 11 | 1 | B608, MEDIUM, Case 13 `query.py`, line 13 | 1 |
| SecureAgent-guided | 11 | 0 | No findings | 0 |

Both runs pass all 11 tests. The measured difference is removal of the residual required B608 finding.

## 8. Reproduce the Original Ten-Case Harness

Vulnerable source command:

```powershell
& $python -m pytest evaluation/cases -q
```

Expected result:

- Progress pattern: `.F.F.F.F.F.F.F.F.F.F`
- `10 failed, 10 passed`
- Exit code: 1
- Clean-reproduction runtime: 2.03 seconds
- Each functional test passes and each security test fails intentionally.

Repaired official baseline command:

```powershell
& $python -m pytest evaluation/runs/baseline_official_02_ten_case -q
```

Expected result:

- `20 passed`
- Exit code: 0
- Clean-reproduction runtime: 1.24 seconds

## 9. Reproduce the Ten-Case Scanner Evidence

```powershell
$scanRoots = [ordered]@{
    "ten-case source" = "evaluation\cases"
    "ten-case repaired baseline" = "evaluation\runs\baseline_official_02_ten_case"
}

foreach ($entry in $scanRoots.GetEnumerator()) {
    $appFiles = Get-ChildItem $entry.Value -Recurse -File -Filter *.py |
        Where-Object {
            $_.Directory.Name -like "case_*" -and
            $_.Name -notin @("__init__.py", "test_vulnerable_app.py", "test_public_behavior.py")
        } |
        ForEach-Object { $_.FullName }

    $safeName = $entry.Key.Replace(" ", "-")
    $outputPath = Join-Path $env:TEMP "secureagent-$safeName-bandit.json"

    & $python -m bandit -f json -o $outputPath @appFiles
    $scanExit = $LASTEXITCODE
    $scanResults = (Get-Content $outputPath -Raw | ConvertFrom-Json).results
    $repoRoot = (Resolve-Path ".").Path

    "`n$($entry.Key):"

    $scanResults | ForEach-Object {
        $relativePath = $_.filename.Substring($repoRoot.Length + 1)
        "$($_.test_id) | $($_.issue_severity) | $relativePath | line $($_.line_number)"
    }

    "application files scanned: $($appFiles.Count)"
    "results count: $($scanResults.Count)"
    "Bandit exit code: $scanExit"
}
```

Expected results:

| Run | Files scanned | Findings | Severity summary | Exit code |
|-----|---|---|---|---|
| Ten-case vulnerable source | 13 | 10 | 3 HIGH, 3 MEDIUM, 4 LOW | 1 |
| Ten-case repaired baseline | 13 | 3 | 3 LOW | 1 |

The three repaired-baseline findings are B404, B607, and B603 in Case 02. All required target findings were removed and no HIGH finding remained.

## 10. Expected Exit Codes

| Command category | Expected exit code | Meaning |
|---|---|---|
| Vulnerable pytest harness | 1 | Intentional security-test failures are present |
| Repaired pytest run | 0 | All functional, regression, and security tests pass |
| Bandit with findings | 1 | Scanner findings are present |
| Bandit with zero findings | 0 | No scanner finding is present |
| `pip check` | 0 | Installed dependencies are consistent |

## 11. Evidence and Methodology

Repository artifacts:

- Hard-holdout protocol: [evaluation/HARD_HOLDOUT_PROTOCOL.md](evaluation/HARD_HOLDOUT_PROTOCOL.md)
- Final comparison: [evaluation/HARD_HOLDOUT_COMPARISON.md](evaluation/HARD_HOLDOUT_COMPARISON.md)
- Generic hard-holdout result: [evaluation/runs/baseline_official_03_hard_holdout/RESULT.md](evaluation/runs/baseline_official_03_hard_holdout/RESULT.md)
- SecureAgent-guided result: [evaluation/runs/secureagent_official_01_hard_holdout/RESULT.md](evaluation/runs/secureagent_official_01_hard_holdout/RESULT.md)
- Generic Bandit evidence: [evaluation/runs/baseline_official_03_hard_holdout/bandit-results.json](evaluation/runs/baseline_official_03_hard_holdout/bandit-results.json)
- Guided before scan: [evaluation/runs/secureagent_official_01_hard_holdout/bandit-before.json](evaluation/runs/secureagent_official_01_hard_holdout/bandit-before.json)
- Guided after scan: [evaluation/runs/secureagent_official_01_hard_holdout/bandit-after-01.json](evaluation/runs/secureagent_official_01_hard_holdout/bandit-after-01.json)
- Improvement changelog: [IMPROVEMENT_CHANGELOG.md](IMPROVEMENT_CHANGELOG.md)
- Build trajectories: [traces/build](traces/build)

The generative agent runs are preserved as committed run directories and trajectories. Their exact prompts, restrictions, human checkpoints, invalid tool attempts, and validation evidence are recorded in the linked result and trajectory documents.

## 12. Runtime and Cost

- Validation runtimes are machine-dependent and should not be treated as performance benchmarks.
- The observed clean-reproduction runtimes are reported only to confirm practical reproducibility.
- No API-token cost was measured.
- Copilot Student Auto did not expose the automatically selected underlying model or a per-run monetary cost.
- No cost estimate is reported because the required usage data was unavailable.

## 13. Safety Notice

- All cases are synthetic evaluation fixtures.
- Vulnerable source directories intentionally contain insecure code and failing security tests.
- They must never be reused in production.
- The fixtures use synthetic identities, payloads, reports, tokens, URLs, and database records.
- The evaluation does not require real credentials, production data, private data, or external-service access.

## 14. Troubleshooting

- Run commands from the repository root.
- In Windows PowerShell, use the call operator `&` before a Python executable stored in a variable.
- Set `SECUREAGENT_HOLDOUT_PACKAGE` immediately before each hard-holdout pytest command.
- A vulnerable-state pytest or Bandit exit code of 1 can be expected.
- Inspect the textual summary before treating a nonzero exit as a setup failure.
- Bandit JSON output is written to the operating-system temporary directory by the reproduction commands.
- Exact runtimes can differ.
- If imports resolve from another clone, confirm the current directory is the clean repository root.
- `python -m pip check` should report no broken requirements.