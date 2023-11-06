def limit_between(n: int, lower: int, upper: int) -> int:
    return (n - lower) % (upper - lower + 1) + lower