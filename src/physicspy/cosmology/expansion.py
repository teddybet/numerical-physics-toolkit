import numpy as np
def hubble_parameter(
    scale_factor,
    hubble_constant=70.0,
    omega_matter=0.3,
    omega_lambda=0.7,
):
    """
    Calculate the Hubble parameter H(a) for a flat
    matter + dark-energy universe.
    Parameters
    ----------
    scale_factor : float
        Cosmological scale factor a.
    hubble_constant : float
        Present-day Hubble constant H0 in km/s/Mpc.
    omega_matter : float
        Present-day matter density parameter.
    omega_lambda : float
        Present-day dark-energy density parameter.
    Returns
    -------
    float
        Hubble parameter H(a) in km/s/Mpc.
    """
    if scale_factor <= 0:
        raise ValueError(
            "Scale factor must be greater than zero."
        )
    return hubble_constant * np.sqrt(
        omega_matter / scale_factor**3
        + omega_lambda
    )
def expansion_rate(
    scale_factor,
    hubble_constant=70.0,
    omega_matter=0.3,
    omega_lambda=0.7,
):
    """
    Calculate da/dt up to the units associated
    with the supplied Hubble parameter.
    """
    return scale_factor * hubble_parameter(
        scale_factor,
        hubble_constant,
        omega_matter,
        omega_lambda,
    )