import numpy as np
import pytest
from physicspy.quantum.particle_in_box import (
    wavefunction,
    probability_density,
    energy_level,
)
def test_wavefunction_boundaries():
    box_length = 1.0
    assert wavefunction(0, 1, box_length) == pytest.approx(0.0)
    assert wavefunction(box_length, 1, box_length) == pytest.approx(0.0)
def test_probability_density_nonnegative():
    x = np.linspace(0, 1, 100)
    density = probability_density(
        x,
        n=1,
        box_length=1.0,
    )
    assert np.all(density >= 0)
def test_energy_increases_with_quantum_number():
    e1 = energy_level(1, 1e-9)
    e2 = energy_level(2, 1e-9)
    assert e2 > e1
def test_energy_scaling():
    e1 = energy_level(1, 1e-9)
    e2 = energy_level(2, 1e-9)
    assert e2 == pytest.approx(4 * e1)
def test_invalid_quantum_number():
    with pytest.raises(ValueError):
        wavefunction(
            x=0.5,
            n=0,
            box_length=1.0,
        )