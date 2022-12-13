"""Example code."""
import result


def some_function(first: int, second: int) -> result.Result[float, Exception]:
    """We use this function as an example for some real logic."""
    if second == 0:
        return result.Err(ZeroDivisionError())
    elif second >= 10:
        return result.Err(ValueError("Value is to big"))
    return result.Ok(first / second)
