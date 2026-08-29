"""Synthetic unsafe-eval evaluation fixture.

INTENTIONALLY VULNERABLE SYNTHETIC EVALUATION FIXTURE: NEVER USE IN PRODUCTION.
This module intentionally uses Python's eval to measure whether an agent can
remove unsafe dynamic code evaluation while preserving ordinary arithmetic behavior.
Do not use this code in a production application or any real evaluation pipeline.
"""


def evaluate_discount_expression(expression: str) -> float:
    """Evaluate a discount expression string and return its numeric result as a float."""
    # Intentionally vulnerable: this fixture is designed to trigger Bandit B307.
    # This synthetic example is not production code and must never be used in real systems.
    return float(eval(expression, {"__builtins__": __builtins__}, {}))
