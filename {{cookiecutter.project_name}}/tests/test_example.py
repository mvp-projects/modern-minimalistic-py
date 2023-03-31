"""Example test."""

import pytest
from typing import Type
from {{cookiecutter.project_name.lower().replace('-', '_')}}.example import some_function


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
    resp = some_function(first, second)
    if isinstance(resp, Ok):
        assert resp.unwrap() == pytest.approx(expected)
    else:
        raise TypeError


@pytest.mark.parametrize(
    ("first", "second", "expected_err_type"),
    [
        (1, 0, ZeroDivisionError),
        (1, 11, ValueError),
    ],
)
def test_some_function_fails(
    first: int,
    second: int,
    expected_err_type: type[Exception],
) -> None:
    """Test failure."""
    resp = some_function(first, second)
    if isinstance(
        resp,
        Ok,
    ) or not isinstance(
        resp.err(),
        expected_err_type,
    ):
        raise TypeError

    assert True
