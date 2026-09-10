def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h


def backward_difference(f, x, h):
    return (f(x) - f(x - h)) / h


def central_difference(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

def forward_second_difference(f, x, h):
    return (f(x + 2*h) - 2*f(x + h) + f(x)) / h**2


def backward_second_difference(f, x, h):
    return (f(x) - 2*f(x - h) + f(x - 2*h)) / h**2


def central_second_difference(f, x, h):
    return (f(x + h) - 2*f(x) + f(x - h)) / h**2

