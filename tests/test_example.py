"""Example test."""

import pytest

from sample.example import some_function
from returns import result


@pytest.mark.parametrize(
    ("first", "second", "expected"),
    [
        (1, 2, 0.5),
        (2, 4, 0.5),
        (-2, -3, 0.6666666),
        (-5, 5, -1),
    ],
)
def test_some_function(first: int, second: int, expected: int) -> None:
    """Example test with parametrization."""
    result = some_function(first, second).unwrap()
    assert result == pytest.approx(expected)


@pytest.mark.parametrize(
    ("first", "second"),
    [
        (1, 0),
    ],
)
def test_some_function_fails(first: int, second: int) -> None:
    result = some_function(first, second)
    err = result.failure()
    if isinstance(err, ZeroDivisionError):
        assert True
