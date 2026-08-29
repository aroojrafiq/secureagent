import pytest

from .vulnerable_app import evaluate_discount_expression


def test_evaluate_discount_expression_returns_expected_numeric_value():
    """Functional test: ordinary arithmetic must still behave correctly."""
    result = evaluate_discount_expression("100 * 0.20")

    assert result == 20.0


def test_evaluate_discount_expression_rejects_inert_synthetic_payload():
    """Security test: the function should reject the inert synthetic payload."""
    with pytest.raises(ValueError):
        evaluate_discount_expression("__import__('builtins').len('synthetic')")
