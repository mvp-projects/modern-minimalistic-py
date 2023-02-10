"""Example code."""
import result


def some_function(first: int, second: int) -> result.Result[float, Exception]:
    """We use this function as an example for some real logic."""
    upper_bound = 10
    
    if second == 0:
        return result.Err(ZeroDivisionError())

    
    if second >= upper_bound:
        return result.Err(ValueError("Value is to big"))

    return result.Ok(first / second)
