import numpy as np
def wavefunction(x, n, box_length):
    """
    Normalized wavefunction for a particle in a 1D infinite square well.
    Parameters
    ----------
    x : float or array-like
        Position inside the box.
    n : int
        Quantum number. Must be a positive integer.
    box_length : float
        Length of the box.
    Returns
    -------
    float or numpy.ndarray
        Wavefunction value psi_n(x).
    """
    if n <= 0 or not isinstance(n, int):
        raise ValueError("Quantum number n must be a positive integer.")
    if box_length <= 0:
        raise ValueError("Box length must be greater than zero.")
    return np.sqrt(2 / box_length) * np.sin(
        n * np.pi * x / box_length
    )
def probability_density(x, n, box_length):
    """
    Calculate the probability density |psi_n(x)|^2.
    """
    psi = wavefunction(x, n, box_length)
    return np.abs(psi) ** 2
def energy_level(
    n,
    box_length,
    particle_mass=9.1093837e-31,
    hbar=1.054571817e-34,
):
    """
    Calculate the energy of a particle in a 1D infinite square well.
    Parameters
    ----------
    n : int
        Quantum number.
    box_length : float
        Box length in meters.
    particle_mass : float
        Particle mass in kilograms.
    hbar : float
        Reduced Planck constant.
    Returns
    -------
    float
        Energy in joules.
    """
    if n <= 0 or not isinstance(n, int):
        raise ValueError("Quantum number n must be a positive integer.")

    if box_length <= 0:
        raise ValueError("Box length must be greater than zero.")
    return (
        n**2
        * np.pi**2
        * hbar**2
        / (2 * particle_mass * box_length**2)
    )