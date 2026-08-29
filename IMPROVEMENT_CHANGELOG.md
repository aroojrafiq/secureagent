# Improvement Changelog

| Stage | What We Tried and Why | Evidence | Decision or Learning |
|---|---|---|---|
| Baseline | Generic Copilot Auto baseline with one repair pass and no scanners, ground truth, or retries. The first run was invalidated because the Case 02 functional test was over-constrained. | [Result](evaluation/runs/baseline_official_01/RESULT.md); [Trace](traces/build/006-generic-baseline-official-01.md); [Bandit evidence](evaluation/runs/baseline_official_01/bandit-results.json) | Corrected rerun: agent pytest 6/6; evaluator pytest 6/6; B608, B602, and B105 absent; only low-severity B404, B607, and B603 remained. Preliminary rate: 3/3 (100%). These first three cases are too easy; harder and multi-file cases are required before final comparison. |
| Iteration 1 | _Placeholder: describe the first improvement attempted and why._ | _Placeholder: link or describe supporting evidence._ | _Placeholder: record the decision or learning._ |
| Iteration 2 | _Placeholder: describe the second improvement attempted and why._ | _Placeholder: link or describe supporting evidence._ | _Placeholder: record the decision or learning._ |
| Removed Experiment | First generic baseline attempt using the initial three-case harness | [evaluation/runs/baseline_invalidated_01/RESULT.md](evaluation/runs/baseline_invalidated_01/RESULT.md); [traces/build/005-generic-baseline-run-01-invalidated.md](traces/build/005-generic-baseline-run-01-invalidated.md) | Excluded from all metrics because the Case 02 functional test over-constrained the command representation; corrected the harness and reran from fresh copies. |
| Final | _Placeholder: summarize the final approach._ | _Placeholder: link or describe final evidence._ | _Placeholder: record final decisions and remaining questions._ |
