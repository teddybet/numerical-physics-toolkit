import pytest
from physicspy.cosmology.redshift import (
    redshift_from_wavelength,
)
def test_redshift():
    result = redshift_from_wavelength(
        observed_wavelength=600,
        emitted_wavelength=500,
    )
    assert result == pytest.approx(0.2)
def test_no_redshift():
    result = redshift_from_wavelength(
        observed_wavelength=500,
        emitted_wavelength=500,
    )
    assert result == pytest.approx(0.0)
def test_invalid_emitted_wavelength():
    with pytest.raises(ValueError):
        redshift_from_wavelength(
            observed_wavelength=600,
            emitted_wavelength=0,
        )