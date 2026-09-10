import pytest
from physicspy.numerical_methods.secant import secant
def test_secant():
    def f(x):
        return x**3 - 6*x**2 + 11*x - 6.1
    root, error, iterations = secant(f, 2.5, 3.5, 0.01)
    assert abs(root - 3.047) < 0.01
    assert error < 0.01
    assert iterations > 0
def test_zero_denominator():
    def f(x):
        return x**2
    with pytest.raises(ZeroDivisionError):
        secant(f, 1, -1, 0.01)