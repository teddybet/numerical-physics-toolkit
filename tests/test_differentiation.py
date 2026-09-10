from physicspy.numerical_methods.differentiation import (
    forward_difference,
    backward_difference,
    central_difference,
    forward_second_difference,
    backward_second_difference,
    central_second_difference,
)
def test_first_derivatives():
    def f(x):
        return x**2
    exact = 4
    assert abs(forward_difference(f, 2, 0.1) - exact) < 0.2
    assert abs(backward_difference(f, 2, 0.1) - exact) < 0.2
    assert abs(central_difference(f, 2, 0.1) - exact) < 0.01
def test_second_derivatives():
    def f(x):
        return x**2
    exact = 2
    assert abs(forward_second_difference(f, 2, 0.1) - exact) < 0.01
    assert abs(backward_second_difference(f, 2, 0.1) - exact) < 0.01
    assert abs(central_second_difference(f, 2, 0.1) - exact) < 0.01