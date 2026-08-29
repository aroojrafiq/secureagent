# Build Trajectory: Initial Documentation Scaffold

## 1. Metadata

- Date: 2026-08-28
- Coding agent: GitHub Copilot in VS Code Agent mode
- Model policy: Copilot Student Auto model selection
- The underlying model was selected automatically and is not claimed to be known.

## 2. Goal

Establish SecureAgent's initial documentation and governance scaffold without implementing application code.

## 3. Original User Task

You are helping initialise a new hackathon repository named SecureAgent.

Project purpose:
SecureAgent is an evidence-driven security review workflow for AI-generated Python code. It will use deterministic security scanners, agent reasoning, functional tests, security re-scanning, and a human approval checkpoint before a patch is accepted.

For this task, create only the initial documentation and governance scaffold.

Create or update these files:

1. README.md
   Include:
   - Project title and one-sentence description
   - Intended user
   - Problem and bottleneck
   - Version 1 scope: Python projects only
   - Planned workflow: scan, interpret, repair, verify, human approval
   - Current status: initial hackathon development
   - A statement that the repository was created from scratch during the micro1 Agentic Workflows Hackathon and no application code existed before the competition

2. .github/copilot-instructions.md
   Include concise repository-wide rules:
   - Never add credentials, tokens, or private data
   - Make minimal, reviewable changes
   - Use synthetic security fixtures only
   - Run relevant tests and security scans after code changes
   - Never commit, push, merge, or perform consequential actions without human approval
   - Explain security-relevant changes and remaining risks
   - Preserve evidence required for evaluation and reproducibility

3. IMPROVEMENT_CHANGELOG.md
   Create a table with columns:
   Stage, What We Tried and Why, Evidence, Decision or Learning
   Add an empty Baseline row and placeholders for Iteration 1, Iteration 2, Removed Experiment, and Final.

4. REPRODUCTION.md
   Add clearly marked placeholders for prerequisites, clean setup, baseline command, SecureAgent command, evaluation command, expected output, versions, runtime, and cost.

5. evaluation/README.md
   Explain that the same synthetic cases will be used for the baseline and final agent. Record the planned primary metric: verified vulnerability resolution rate.

6. traces/build/README.md
   Explain that this folder will contain representative GitHub Copilot build-session trajectories.

7. traces/runtime/README.md
   Explain that this folder will contain representative SecureAgent runtime trajectories, including instructions, tool results, retries, and human checkpoints.

Constraints:
- Do not implement application code yet.
- Do not create vulnerability fixtures yet.
- Do not install dependencies.
- Do not run terminal commands.
- Do not commit or push anything.
- Preserve the existing LICENSE and .gitignore.
- Do not invent evaluation results.

After making the files, provide a concise summary of exactly what changed.

## 4. Initial Repository State

- Existing README contained only the project title and tagline.
- LICENSE and .gitignore already existed.
- No application code existed.

## 5. Agent Actions and Tool Observations

- Inspected the existing README.
- Inspected the repository directory contents, including the existing README, LICENSE, and .gitignore.
- Created or modified the following files:
  - README.md
  - .github/copilot-instructions.md
  - IMPROVEMENT_CHANGELOG.md
  - REPRODUCTION.md
  - evaluation/README.md
  - traces/build/README.md
  - traces/runtime/README.md
- No terminal commands, installations, commits, or pushes were performed.

## 6. Constraints Followed

- Documentation only.
- No invented results.
- No credentials or private information.
- Existing LICENSE and .gitignore preserved.

## 7. Human Checkpoint

- The generated files were reviewed individually by a human before acceptance.
- The contents were accepted.
- No Git commit or push has happened yet.

## 8. Outcome

The accepted seven-file documentation scaffold consists of:

- README.md
- .github/copilot-instructions.md
- IMPROVEMENT_CHANGELOG.md
- REPRODUCTION.md
- evaluation/README.md
- traces/build/README.md
- traces/runtime/README.md
