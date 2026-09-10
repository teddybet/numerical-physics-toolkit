def trapezoidal(f, a, b):
    return (b - a) * (f(a) + f(b)) / 2
def composite_trapezoidal(f, a, b, n):
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        total += 2 * f(x)
    return h * total / 2
def simpson_one_third(f, a, b):
    midpoint = (a + b) / 2
    return (b - a) * (
        f(a) + 4 * f(midpoint) + f(b)
    ) / 6
def composite_simpson_one_third(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be even for composite Simpson's 1/3 rule.")
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            total += 2 * f(x)
        else:
            total += 4 * f(x)
    return h * total / 3
def simpson_three_eighths(f, a, b):
    h = (b - a) / 3
    return (
        3 * h / 8
        * (
            f(a)
            + 3 * f(a + h)
            + 3 * f(a + 2 * h)
            + f(b)
        )
    )
