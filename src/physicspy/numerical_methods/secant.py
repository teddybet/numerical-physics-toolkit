def secant(f, x_previous, x_current, es, max_iterations=100):
    ea = float('inf')
    iterations = 0

    while ea > es and iterations < max_iterations:
        denominator = f(x_previous) - f(x_current)

        if denominator == 0:
            raise ZeroDivisionError(
                "Secant method cannot continue because the denominator is zero."
            )

        x_new = x_current - (
            f(x_current) * (x_previous - x_current)
            / denominator
        )

        if f(x_new) == 0:
            ea = 0
            iterations += 1
            break

        ea = abs((x_new - x_current) / x_new) * 100

        x_previous = x_current
        x_current = x_new
        iterations += 1

    if ea > es:
        raise RuntimeError("Maximum number of iterations reached.")

    return x_new, ea, iterations
