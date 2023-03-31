"""Example code."""

from result import Err, Ok, Result


def some_function(first: int, second: int) -> Result[float, Exception]:
    """We use this function as an example for some real logic."""
    upper_bound = 10

    if second == 0:
        return Err(ZeroDivisionError())

    if second >= upper_bound:
        return Err(ValueError("Value is to big"))

    return Ok(first / second)
