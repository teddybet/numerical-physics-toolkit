import pytest
from physicspy.cosmology.hubble import recession_velocity
def test_recession_velocity():
    result = recession_velocity(100)
    assert result == pytest.approx(7000.0)
def test_custom_hubble_constant():
    result = recession_velocity(
        distance_mpc=100,
        hubble_constant=67.4,
    )
    assert result == pytest.approx(6740.0)
def test_negative_distance():
    with pytest.raises(ValueError):
        recession_velocity(-10)