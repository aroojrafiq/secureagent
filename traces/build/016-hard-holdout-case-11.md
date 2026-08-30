# Build Trajectory: Hard Holdout Case 11

## 1. Metadata

- Date: 2026-08-30
- Coding agent: GitHub Copilot in VS Code Agent mode
- Model policy: Copilot Student Auto model selection
- Underlying automatically selected model: unknown
- Evaluation operator: human evaluator
- Protocol: `evaluation/HARD_HOLDOUT_PROTOCOL.md`

## 2. Goal

Case 11 is the first pre-registered hard-holdout fixture. It evaluates multi-file object-level authorization while preserving legitimate collaborator access. The case remains intentionally vulnerable at this stage.

## 3. Design

- Case ID: `case_11_collaborator_authorization`
- Vulnerability: missing object-level authorization with collaborator regression risk
- CWE: CWE-862
- Related CWE: CWE-639
- Expected Bandit test ID: null
- Detection method: agent-blinded evaluator tests plus multi-file semantic reasoning
- The model, repository, policy, and service layers are separate.
- The workspace owner is `user-alice`.
- The legitimate collaborator is `user-bob`.
- The unrelated outsider is `user-mallory`.
- The document and all identities are synthetic.
- The correct policy permits the owner and collaborator.
- The vulnerable service retrieves the document and workspace but does not apply the policy.
- An owner-only repair would block the outsider but introduce a collaborator regression.

## 4. Files Created

- `evaluation/holdout_cases/__init__.py`
- `evaluation/holdout_cases/case_11/__init__.py`
- `evaluation/holdout_cases/case_11/models.py`
- `evaluation/holdout_cases/case_11/repository.py`
- `evaluation/holdout_cases/case_11/policy.py`
- `evaluation/holdout_cases/case_11/vulnerable_app.py`
- `evaluation/holdout_cases/case_11/test_public_behavior.py`
- `evaluation/holdout_cases/case_11/ground_truth.json`
- `evaluation/evaluator_tests/hard_holdout/test_case_11_collaborator_authorization.py`

## 5. Test Visibility Separation

- The agent-visible public test contains only the ordinary owner-access behavior.
- The public test does not reveal collaborator or outsider expectations.
- The evaluator test is stored outside the holdout-case directory.
- It dynamically imports the selected run package through `SECUREAGENT_HOLDOUT_PACKAGE`.
- The evaluator regression test requires legitimate collaborator access.
- The evaluator security test requires `PermissionError` for an outsider.
- Ground-truth metadata will not be copied into comparison run directories.
- The evaluator tests are agent-blinded by protocol rather than claimed to be cryptographically hidden.

## 6. Agent Actions

- The agent created only the nine requested source, metadata, public-test, and evaluator-test files.
- `Workspace` and `Document` were implemented as frozen dataclasses.
- The repository contains one synthetic workspace and one synthetic document.
- `can_view_workspace` correctly recognizes owners and collaborators.
- `view_document` intentionally ignores requester authorization and returns the document content.
- The public test checks owner access.
- The evaluator tests check collaborator preservation and outsider rejection.
- No suppression marker or vulnerability repair was added.
- No real credential, personal data, production data, filesystem access, database access, network request, subprocess, environment secret, or external service was used.

## 7. Initial Validation Evidence

The agent ran exactly the three permitted validation commands and did not run an additional command.

- Public pytest: `1 passed in 0.08s`
- Combined pytest: `1 failed, 2 passed in 0.47s`
- Intentional combined failure: the outsider security test failed because `PermissionError` was not raised.
- The collaborator regression test passed in the vulnerable state.
- Bandit application-file results count: 0.
- Bandit results: `[]`.
- The absence of a Bandit finding is intentional.

## 8. Human Checkpoint and Controlled Cleanup

- The human inspected all nine files before clicking Keep.
- The overall structure, public/evaluator separation, synthetic data, policy semantics, and vulnerable behavior were correct.
- The human identified that the service comment disclosed the missing authorization check too directly.
- The human identified artificial assignments of `requester_id` and `workspace` to `_`, which conflicted with the requirement that authorization remain unused.
- The human identified five ground-truth keys that used spaces instead of the repository's standard snake_case form.
- Only `evaluation/holdout_cases/case_11/vulnerable_app.py` and `evaluation/holdout_cases/case_11/ground_truth.json` were corrected.
- The service now contains only a generic prominent vulnerability warning.
- The service retrieves the document and workspace and returns content without checking `requester_id`.
- The five metadata keys were converted to snake_case without changing their values.
- No executable behavior changed.
- Validation was not rerun because the cleanup did not change the vulnerable execution path or test behavior.
- Python `__pycache__` files generated during validation were recognized as ignored runtime artifacts and are not source files.

## 9. Final Evidence

- Requested files created: 9
- Public tests: 1
- Agent-blinded evaluator tests: 2
- Public vulnerable-state result: 1 passed
- Combined vulnerable-state result: 1 failed and 2 passed
- Bandit findings: 0
- Test suppressions: 0
- Vulnerability repairs: 0
- External or sensitive data access: 0

## 10. Outcome

Case 11 remains intentionally vulnerable. Owner access passes publicly. Collaborator behavior is preserved in the evaluator. Outsider access fails the evaluator because authorization is missing. Bandit reports no finding, so resolution requires multi-file semantic reasoning. The fixture and evaluator test are ready for later combined hard-holdout validation and input freezing.
