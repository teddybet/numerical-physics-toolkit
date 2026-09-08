def bisection(f, xl, xu, es, max_iterations=100):
    """
    Find a root of a function using the bisection method.

    Parameters
    ----------
    f : function
        The function whose root is being found.
    xl : float
        Lower bound of the interval.
    xu : float
        Upper bound of the interval.
    es : float
        Stopping criterion as a percent relative error.
    max_iterations : int
        Maximum number of iterations allowed.

    Returns
    -------
    root : float
        Approximate root.
    error : float
        Approximate percent relative error.
    iterations : int
        Number of iterations performed.
    """
    
    if f(xl) == 0:
        return xl, 0, 0

    if f(xu) == 0:
        return xu, 0, 0

    if f(xl) * f(xu) > 0:
        raise ValueError("The interval does not bracket a root.")

    xr_old = None
    ea = float('inf')
    iterations = 0
    history = []

    while ea > es and iterations < max_iterations:
        xr = (xl + xu) / 2

        if f(xl) * f(xr) < 0:
            xu = xr
        else:
            xl = xr

        if xr_old is not None:
            ea = abs((xr - xr_old) / xr) * 100

        xr_old = xr
        iterations += 1
        history.append((iterations, xl, xu, xr, ea))
    if ea > es:
            raise RuntimeError("Maximum number of iterations reached.")
    return xr, ea, iterations, history
