def recession_velocity(distance_mpc, hubble_constant=70.0):
    """
    Calculate recession velocity using Hubble's law.
    Parameters
    ----------
    distance_mpc : float
        Distance to the galaxy in megaparsecs.
    hubble_constant : float
        Hubble constant in km/s/Mpc.
    Returns
    -------
    float
        Recession velocity in km/s.
    """
    if distance_mpc < 0:
        raise ValueError("Distance cannot be negative.")
    return hubble_constant * distance_mpc