def while_fib(n: int):
    """
    Returns the value of the given integer, in fibonacci sequence.
    >>> while_fib(5)
    5
    """
    zero_term = 0
    first_term = 1
    current_term = 0

    while current_term < n:
        next_term = zero_term + first_term
        zero_term = first_term
        first_term = next_term

        current_term += 1

    return zero_term
