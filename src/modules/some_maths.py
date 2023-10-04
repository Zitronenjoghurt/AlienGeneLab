def limit_between(n, lower, upper):
    return (n - lower) % (upper - lower + 1) + lower