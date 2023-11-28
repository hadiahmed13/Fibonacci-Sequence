def fib(n: int) -> int:
    """
    returns the term on the given integer in the fibonacci sequence
    >>> fib(5)
    5
    """

    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
