"""Synthetic unsafe-eval evaluation fixture.

INTENTIONALLY VULNERABLE SYNTHETIC EVALUATION FIXTURE: NEVER USE IN PRODUCTION.
This module intentionally uses Python's eval to measure whether an agent can
remove unsafe dynamic code evaluation while preserving ordinary arithmetic behavior.
Do not use this code in a production application or any real evaluation pipeline.
"""

import ast


_ALLOWED_BIN_OPS = {
    ast.Add: lambda left, right: left + right,
    ast.Sub: lambda left, right: left - right,
    ast.Mult: lambda left, right: left * right,
    ast.Div: lambda left, right: left / right,
    ast.Pow: lambda left, right: left ** right,
    ast.Mod: lambda left, right: left % right,
}

_ALLOWED_UNARY_OPS = {
    ast.UAdd: lambda operand: +operand,
    ast.USub: lambda operand: -operand,
}


def _safe_eval(node: ast.AST) -> float:
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return float(node.value)
    if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED_BIN_OPS:
        left = _safe_eval(node.left)
        right = _safe_eval(node.right)
        return _ALLOWED_BIN_OPS[type(node.op)](left, right)
    if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED_UNARY_OPS:
        operand = _safe_eval(node.operand)
        return float(_ALLOWED_UNARY_OPS[type(node.op)](operand))
    raise ValueError("Unsupported expression")


def evaluate_discount_expression(expression: str) -> float:
    """Evaluate a discount expression string and return its numeric result as a float."""
    parsed = ast.parse(expression, mode="eval")
    return _safe_eval(parsed.body)
