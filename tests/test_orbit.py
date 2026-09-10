import numpy as np
import pytest
from physicspy.mechanics.orbit import (
    gravitational_acceleration,
    simulate_orbit,
)
def test_gravitational_acceleration():
    sun_mass = 1.989e30
    earth_distance = 1.496e11
    acceleration = gravitational_acceleration(
        [earth_distance, 0],
        sun_mass,
    )
    assert acceleration[0] == pytest.approx(-0.00593, abs=0.00001)
    assert acceleration[1] == pytest.approx(0.0)
def test_orbit_output():
    times, positions = simulate_orbit(
        initial_position=[1.496e11, 0],
        initial_velocity=[0, 29_780],
        central_mass=1.989e30,
        time_step=3600,
        total_time=24 * 3600,
    )
    assert len(times) == len(positions)
    assert positions.shape[1] == 2
    assert np.all(np.isfinite(positions))
def test_zero_distance():
    with pytest.raises(ZeroDivisionError):
        gravitational_acceleration(
            [0, 0],
            1.989e30,
        )