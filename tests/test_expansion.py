import pytest
from physicspy.cosmology.expansion import (
    hubble_parameter,
    expansion_rate,
)
def test_hubble_parameter_today():
    result = hubble_parameter(
        scale_factor=1.0,
        hubble_constant=70.0,
        omega_matter=0.3,
        omega_lambda=0.7,
    )
    assert result == pytest.approx(70.0)
def test_hubble_parameter_early_universe():
    early = hubble_parameter(0.5)
    today = hubble_parameter(1.0)
    assert early > today
def test_expansion_rate():
    result = expansion_rate(1.0)
    assert result == pytest.approx(70.0)
def test_invalid_scale_factor():
    with pytest.raises(ValueError):
        hubble_parameter(0)