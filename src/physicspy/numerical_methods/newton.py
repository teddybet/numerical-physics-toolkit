def newton(f, df, x0, es, max_iterations=100):
    ea = float('inf')
    x_old = x0
    iterations = 0
    while ea > es:
        if df(x_old) == 0:
            raise ZeroDivisionError("Derivative is zero. Newton's method cannot continue.")
        x_new = x_old - f(x_old) / df(x_old)
        if f(x_new) == 0:
            ea = 0
            iterations += 1
            break
        ea = abs((x_new - x_old) / x_new) * 100
        x_old = x_new
        iterations += 1
    if ea > es:
        raise RuntimeError("Maximum number of iterations reached.")
    return x_new, ea, iterations



def f(x):
    return -0.9*x**2 + 1.7*x + 2.5


def df(x):
    return -1.8*x + 1.7


root = newton(f, df, 5, 0.01)
print(root)