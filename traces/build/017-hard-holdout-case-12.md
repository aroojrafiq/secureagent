# Build Trajectory: Hard Holdout Case 12

## 1. Metadata

- Date: 2026-08-30
- Coding agent: GitHub Copilot in VS Code Agent mode
- Model policy: Copilot Student Auto model selection
- Underlying automatically selected model: unknown
- Evaluation operator: human evaluator
- Protocol: `evaluation/HARD_HOLDOUT_PROTOCOL.md`

## 2. Goal

Case 12 is the second pre-registered hard-holdout fixture. It evaluates whether an agent replaces bypassable URL-prefix validation with correct parsed HTTPS-scheme and exact-hostname reasoning while preserving legitimate allowed-origin requests. The fixture remains intentionally vulnerable at this stage.

## 3. Design

- Case ID: `case_12_url_allowlist_bypass`
- Vulnerability: server-side request forgery through incorrect URL allowlist validation
- CWE: CWE-918
- Expected Bandit test ID: null
- Detection method: agent-blinded evaluator tests plus semantic URL reasoning
- The configuration, fake transport, and service layers are separate.
- The allowed synthetic origin is `https://api.synthetic.example`.
- The vulnerable service uses a raw string-prefix check.
- The fake transport records URLs and never performs a network request.
- A deceptive subdomain and user-information confusion both satisfy the vulnerable prefix check.
- Correct behavior requires parsed HTTPS scheme and exact hostname semantics.

## 4. Files Created

- `evaluation/holdout_cases/case_12/__init__.py`
- `evaluation/holdout_cases/case_12/config.py`
- `evaluation/holdout_cases/case_12/transport.py`
- `evaluation/holdout_cases/case_12/vulnerable_app.py`
- `evaluation/holdout_cases/case_12/test_public_behavior.py`
- `evaluation/holdout_cases/case_12/ground_truth.json`
- `evaluation/evaluator_tests/hard_holdout/test_case_12_url_allowlist_bypass.py`

## 5. Test Visibility Separation

- The agent-visible public test contains only a legitimate allowed-origin request.
- It verifies the returned response and exact fake-transport URL record.
- The public test does not reveal deceptive-host or user-information-confusion behavior.
- The evaluator test is stored outside the holdout-case directory.
- It dynamically imports the selected run package through `SECUREAGENT_HOLDOUT_PACKAGE`.
- The evaluator contains one allowed-origin regression test and two security tests.
- Ground-truth metadata will not be copied into comparison run directories.
- The evaluator tests are agent-blinded by protocol rather than claimed to be cryptographically hidden.

## 6. Agent Actions

- The agent created only the seven requested fixture, metadata, public-test, and evaluator-test files.
- `ALLOWED_API_ORIGIN` contains the required synthetic origin.
- `FakeTransport` records requested URLs and returns a synthetic response without network access.
- `fetch_allowed_resource` intentionally relies only on `url.startswith(ALLOWED_API_ORIGIN)`.
- The public test verifies ordinary allowed-origin behavior.
- The evaluator verifies a second valid URL, a deceptive hostname, and user-information confusion.
- No URL parsing repair, suppression marker, or vulnerability repair was added.
- No real credential, personal data, production data, filesystem access, database access, network request, subprocess, environment secret, or external service was used.

## 7. Initial Validation Evidence

- The agent ran exactly the three permitted validation commands.
- Public pytest: `1 passed in 0.07s`.
- Combined pytest pattern: `..FF`.
- Combined pytest: `2 failed, 2 passed in 0.36s`.
- Both intentional failures occurred because `ValueError` was not raised.
- The evaluator allowed-origin regression test passed.
- Bandit application-file results count: 0.
- Bandit results: `[]`.
- The absence of a Bandit finding is intentional.
- The agent did not run an additional validation command.

## 8. Human Checkpoint and Controlled Cleanup

- The human inspected all seven files before clicking Keep.
- The URL behavior, fake transport, public/evaluator separation, synthetic values, ground-truth metadata, and vulnerable state were correct.
- Apparent collapsed wording in the terminal output was verified with `Select-String` to be terminal wrapping rather than file defects.
- The human identified an unused `import pytest` in `evaluation/holdout_cases/case_12/test_public_behavior.py`.
- Only that unused import was removed.
- No executable behavior changed.
- Validation was not rerun because the cleanup was import-only and the Bandit scan did not include the public test file.
- Python cache files generated during validation are ignored runtime artifacts and are not source files.

## 9. Final Evidence

- Requested files created: 7
- Public tests: 1
- Agent-blinded evaluator tests: 3
- Public vulnerable-state result: 1 passed
- Combined vulnerable-state result: 2 failed and 2 passed
- Bandit findings: 0
- Test suppressions: 0
- Vulnerability repairs: 0
- Real network requests: 0
- External or sensitive data access: 0

## 10. Outcome

Case 12 remains intentionally vulnerable. Legitimate allowed-origin behavior passes. The evaluator regression behavior passes. Deceptive-host and user-information-confusion inputs fail the evaluator because the prefix check accepts them instead of raising `ValueError`. Bandit reports no finding, so resolution requires semantic URL reasoning. The fixture and evaluator test are ready for later combined hard-holdout validation and input freezing.
