"""Example code."""
from returns import result


def some_function(first: int, second: int) -> result.Result[float, Exception]:
    """We use this function as an example for some real logic."""
    if second == 0:
        return result.Failure(ZeroDivisionError())
    return result.Success(first / second)
