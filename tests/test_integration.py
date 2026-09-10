from physicspy.numerical_methods.integration import (
    trapezoidal,
    composite_trapezoidal,
    simpson_one_third,
    composite_simpson_one_third,
    simpson_three_eighths,
)
def test_trapezoidal():
    def f(x):
        return x**2
    result = trapezoidal(f, 0, 2)
    assert abs(result - 4.0) < 0.0001
def test_composite_trapezoidal():
    def f(x):
        return x**2
    result = composite_trapezoidal(f, 0, 2, 4)
    assert abs(result - 2.75) < 0.0001
def test_simpson_one_third():
    def f(x):
        return x**2
    result = simpson_one_third(f, 0, 2)
    assert abs(result - 8/3) < 0.0001
def test_composite_simpson_one_third():
    def f(x):
        return x**2
    result = composite_simpson_one_third(f, 0, 2, 4)
    assert abs(result - 8/3) < 0.0001
def test_simpson_three_eighths():
    def f(x):
        return x**2
    result = simpson_three_eighths(f, 0, 2)
    assert abs(result - 8/3) < 0.0001