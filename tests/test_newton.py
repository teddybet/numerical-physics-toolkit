import pytest
from physicspy.numerical_methods.newton import newton
def test_newton():
    def f(x):
        return -0.9*x**2 + 1.7*x + 2.5
    def df(x):
        return -1.8*x + 1.7
    root, error, iterations = newton(f, df, 5, 0.01)
    assert abs(root - 2.860104) < 0.001
    assert error < 0.01
    assert iterations > 0
def test_zero_derivative():
    def f(x):
        return x**2 + 1
    def df(x):
        return 2*x
    with pytest.raises(ZeroDivisionError):
        newton(f, df, 0, 0.01)