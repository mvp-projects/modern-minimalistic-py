"""Example test."""

import pytest
from typing import Type
from sample.example import some_function


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
    value = some_function(first, second)
    err = value.err()
    if not err:
        assert value.unwrap() == pytest.approx(expected)
    else:
        assert False


@pytest.mark.parametrize(
    ("first", "second", "expected_err_type"),
    [
        (1, 0, ZeroDivisionError),
    ],
)
def test_some_function_fails(
    first: int, second: int, expected_err_type: Type[Exception]
) -> None:
    value = some_function(first, second)
    err = value.err()
    if not err:
        assert False
    else:
        if isinstance(err, expected_err_type):
            assert True
        else:
            assert False
