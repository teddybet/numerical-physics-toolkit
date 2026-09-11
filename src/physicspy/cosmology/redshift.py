def redshift_from_wavelength(
    observed_wavelength,
    emitted_wavelength,
):
    """
    Calculate cosmological redshift from wavelengths.
    Parameters
    ----------
    observed_wavelength : float
        Observed wavelength.
    emitted_wavelength : float
        Emitted/rest wavelength.
    Returns
    -------
    float
        Cosmological redshift.
    """
    if emitted_wavelength <= 0:
        raise ValueError(
            "Emitted wavelength must be greater than zero."
        )
    if observed_wavelength <= 0:
        raise ValueError(
            "Observed wavelength must be greater than zero."
        )
    return (
        observed_wavelength - emitted_wavelength
    ) / emitted_wavelength