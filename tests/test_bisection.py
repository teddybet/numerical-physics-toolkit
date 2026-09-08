import pytest
from physicspy.numerical_methods.bisection import bisection
def test_bisection():
    def f(x):
        return x**2 - 2

    root, error, iterations, history = bisection(f, 1, 2, 1)

    assert abs(root - 1.41421356) < 0.01
    assert len(history) == iterations
def test_invalid_interval():
    def f(x):
        return x**2 - 2

    with pytest.raises(ValueError):
        bisection(f, 2, 3, 1)