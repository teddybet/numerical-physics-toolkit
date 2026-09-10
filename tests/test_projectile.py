import pytest
from physicspy.mechanics.projectile import (
    projectile_motion,
    projectile_statistics,
)
def test_projectile_motion():
    times, x, y = projectile_motion(
        initial_speed=30,
        angle_degrees=45,
    )
    assert len(times) > 0
    assert len(times) == len(x) == len(y)
    assert x[0] == pytest.approx(0)
    assert y[0] == pytest.approx(0)
    assert all(y >= 0)
def test_projectile_statistics():
    max_height, flight_time, horizontal_range = projectile_statistics(
        initial_speed=30,
        angle_degrees=45,
    )
    assert max_height == pytest.approx(22.94, abs=0.01)
    assert flight_time == pytest.approx(4.32, abs=0.01)
    assert horizontal_range == pytest.approx(91.74, abs=0.02)