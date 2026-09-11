import numpy as np
import matplotlib.pyplot as plt
from physicspy.quantum.particle_in_box import (
    wavefunction,
    probability_density,
    energy_level,
)
box_length = 1e-9
x = np.linspace(0, box_length, 500)
for n in [1, 2, 3]:
    psi = wavefunction(x, n, box_length)
    plt.plot(
        x * 1e9,
        psi,
        label=f"n = {n}",
    )
plt.xlabel("Position (nm)")
plt.ylabel("Wavefunction ψ(x)")
plt.title("Particle in a 1D Infinite Square Well")
plt.legend()
plt.grid()
plt.savefig(
    "images/particle_in_box_wavefunctions.png",
    dpi=300,
    bbox_inches="tight",
)
plt.show()