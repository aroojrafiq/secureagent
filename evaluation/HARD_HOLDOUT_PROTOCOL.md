# Hard Holdout Comparison Protocol

## 1. Purpose

The original official ten-case generic baseline resolved 10 of 10 cases in one pass. This result remains valid and must not be discarded, altered, or excluded. However, it creates a ceiling for the case-resolution metric and shows that small fixtures with visible security tests can disclose their expected repairs to a capable general coding agent.

The hard holdout phase therefore evaluates realistic multi-file reasoning, regression avoidance, semantic security decisions, scanner-supported detection, verification feedback, and controlled retries.

## 2. Prior Evidence

- Original harness: 10 cases and 20 tests.
- Generic baseline result: 20 passed.
- Cases resolved: 10 of 10.
- Required target findings remaining: 0.
- New high-severity findings: 0.
- Residual findings: B404, B607, and B603, all LOW.
- The result is preserved at `evaluation/runs/baseline_official_02_ten_case`.
- The result summary is `evaluation/runs/baseline_official_02_ten_case/RESULT.md`.
- The trajectory is `traces/build/015-generic-baseline-official-02-ten-case.md`.

## 3. Experimental Design Principles

The experimental design follows these principles:
- Do not design arbitrary tricks solely to force the generic baseline to fail.
- Use realistic vulnerability and regression patterns.
- Freeze all fixtures, evaluator tests, success criteria, prompts, and metrics before either comparison run.
- Give the generic baseline and SecureAgent-guided run byte-identical starting application code and public tests.
- Run both approaches in fresh directories.
- Do not copy ground-truth metadata into either run directory.
- Preserve every result, including unexpected successes and failures.
- Do not tune a fixture after observing either agent's result.
- If a fixture is invalid before the comparison begins, correct and revalidate it before freezing the input snapshot.
- Report original-suite, hard-holdout, and combined metrics separately.

## 4. Holdout Case 11: Collaborator Authorization

Case metadata:
- Case ID: `case_11_collaborator_authorization`
- Vulnerability: missing object-level authorization
- CWE: CWE-862, with CWE-639 as a related object-identifier weakness
- Expected Bandit test ID: null
- Detection basis: agent-blinded evaluator tests plus multi-file semantic reasoning

Fixture design:
- Use separate model, repository, policy, and service modules.
- Store only obviously synthetic workspaces, users, memberships, and documents in memory.
- A workspace has an owner and legitimate collaborators.
- The vulnerable service retrieves and returns a document without applying the policy-layer membership decision.
- The agent-visible functional test verifies ordinary owner access.
- Agent-blinded evaluator tests verify that a legitimate collaborator retains access and an unrelated user receives `PermissionError`.
- An owner-only repair is incomplete because it prevents unauthorized access but introduces a collaborator regression.
- A correct repair follows workspace membership across the model, repository, policy, and service layers.
- No filesystem, database, network, credential, subprocess, or external-service access occurs.

## 5. Holdout Case 12: URL Allowlist Bypass

Case metadata:
- Case ID: `case_12_url_allowlist_bypass`
- Vulnerability: server-side request forgery through incorrect URL allowlist validation
- CWE: CWE-918
- Expected Bandit test ID: null
- Detection basis: agent-blinded evaluator tests plus semantic URL reasoning

Fixture design:
- Use separate configuration, transport, and service modules.
- Use a fake in-memory transport; no network request occurs.
- The allowed synthetic origin is `https://api.synthetic.example`.
- The vulnerable implementation accepts URLs using a string-prefix check.
- The agent-visible functional test verifies a legitimate URL under the allowed origin.
- Agent-blinded evaluator tests verify that normal allowed paths and query strings remain accepted.
- Agent-blinded security tests reject deceptive hosts such as `https://api.synthetic.example.attacker.test/data` and user-information confusion such as `https://api.synthetic.example@attacker.test/data`.
- A correct repair parses the URL and validates the HTTPS scheme and exact hostname rather than trusting a raw string prefix.
- Only synthetic URLs and values are used.

## 6. Holdout Case 13: Dynamic Sort Injection

Case metadata:
- Case ID: `case_13_dynamic_sort_injection`
- Vulnerability: SQL injection through an unvalidated dynamic sort identifier
- CWE: CWE-89
- Expected Bandit test ID: B608
- Detection basis: Bandit plus agent-blinded evaluator tests

Fixture design:
- Use separate model, repository, query, and service modules.
- Use SQLite only with temporary synthetic test data.
- Ordinary filter values are already parameterized.
- The vulnerable query layer interpolates a caller-controlled `sort_by` identifier into an `ORDER BY` clause.
- The agent-visible functional test verifies that one supported sort field produces correct ordering from deliberately unsorted input.
- Agent-blinded regression tests verify all documented supported sort fields.
- Agent-blinded security tests require unsupported or injected sort expressions to raise `ValueError` and confirm that synthetic data remains intact.
- A naive attempt to bind an SQL identifier as a parameter is not a correct repair because it does not preserve ordering semantics.
- A correct repair maps a small allowlist of public sort keys to fixed SQL identifiers.
- No production database, credential, network, subprocess, or external service is used.

## 7. Test Visibility Model

The test-visibility model is:
- Each run directory contains application code, package files, and agent-visible functional tests.
- Ground-truth metadata is excluded.
- Security and regression evaluator tests are stored at `evaluation/evaluator_tests/hard_holdout`.
- The evaluator tests are committed before either run for reproducibility but remain outside both agents' permitted inspection scope.
- These tests are agent-blinded by protocol, not claimed to be cryptographically hidden.
- Both approaches receive the same public tests and the same evaluator command.
- Both agents may observe evaluator failure output when the command is run, but neither may open or inspect the evaluator-test source.

## 8. Evaluator Interface

The frozen evaluator interface is:
- Evaluator tests select the run package through the environment variable `SECUREAGENT_HOLDOUT_PACKAGE`.
- The tests dynamically import Case 11, Case 12, and Case 13 from that package.
- Each comparison run uses the same evaluator tests with only the package value changed.
- The combined validation command runs both the run-directory tests and the external evaluator tests in one pytest invocation.
- Exact runnable commands will be documented and validated before the input snapshots are frozen.

## 9. Generic Baseline Protocol

The generic baseline protocol is:
- Fresh byte-identical input copy.
- Fresh Copilot chat.
- Generic instruction to inspect only the run directory and repair security weaknesses.
- No access to ground truth, evaluator-test source, source fixtures, previous runs, traces, scanners, or SecureAgent guidance.
- One repair pass.
- One combined validation command after editing.
- No retry or edit after that command, regardless of outcome.
- No commit or push by the repair agent.
- Independent human evaluation after the agent stops.

## 10. SecureAgent-Guided Protocol

The SecureAgent-guided protocol is:
- Fresh byte-identical input copy.
- Fresh agent session.
- Same agent-visible code, public tests, and combined evaluator command.
- No access to ground truth or evaluator-test source.
- SecureAgent may use its documented scanner, evidence collection, human approval, verification, and retry workflow.
- Maximum: one initial repair pass plus two evidence-triggered corrective retries.
- Human approval is required before applying each repair or corrective retry.
- Every attempt, command, result, and approval checkpoint is preserved.
- No unrecorded manual repair.
- Independent human evaluation after the workflow stops.

## 11. Case Success Criteria

A holdout case is resolved only when:
1. Its agent-visible functional tests pass.
2. Its agent-blinded security tests pass.
3. Its agent-blinded regression tests pass.
4. Its required target Bandit finding is absent when a target applies.
5. No new high-severity finding is introduced.

A plausible code change that removes the original weakness but breaks legitimate behavior is not counted as resolved.

## 12. Frozen Metrics

Primary metrics:
- Holdout cases attempted and resolved.
- Holdout case-resolution rate.
- Agent-visible functional-test pass rate.
- Agent-blinded security-test pass rate.
- Agent-blinded regression-test pass rate.
- Required target findings remaining.
- New high-severity findings.
- Residual findings by severity.
- Validation attempts.
- Corrective retries.
- Human approval checkpoints.
- Unauthorized file modifications.
- Evidence completeness.

Reporting strata:
- Original ten-case suite.
- Three-case hard holdout.
- Combined thirteen-case suite.

## 13. Freeze and Anti-Overfitting Rules

Freeze and anti-overfitting rules:
- This protocol is written before the three fixtures are implemented or either agent is run.
- Case semantics, public behavior, evaluator behavior, prompts, retry limits, and scoring rules must be finalized before freezing the input snapshot.
- Any pre-freeze correction is documented.
- No post-run case alteration is permitted.
- A tool failure may be rerun only when no valid agent or security result was produced, and the invalid attempt must remain documented.
- Unexpected outcomes are reported rather than tuned away.
- The same acceptance rules apply to both approaches.

## 14. Interpretation

Interpretation rules:
- If both approaches solve all holdouts, the ceiling finding is strengthened and must be reported honestly.
- If SecureAgent improves regression, security, or target-finding outcomes, that improvement is reported with the additional attempts and approvals required.
- If SecureAgent does not improve outcomes, its value may still be evaluated through evidence quality, reproducibility, human control, and auditability, without claiming unsupported remediation improvement.
- The purpose is a credible comparison, not a predetermined win.
