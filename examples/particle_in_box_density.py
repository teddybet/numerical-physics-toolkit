import numpy as np
import matplotlib.pyplot as plt
from physicspy.quantum.particle_in_box import (
    probability_density,
    energy_level,
)
box_length = 1e-9
x = np.linspace(0, box_length, 500)
for n in [1, 2, 3]:
    density = probability_density(
        x,
        n,
        box_length,
    )
    plt.plot(
        x * 1e9,
        density,
        label=f"n = {n}",
    )
plt.xlabel("Position (nm)")
plt.ylabel("Probability Density |ψ(x)|²")
plt.title("Probability Densities in a 1D Infinite Square Well")
plt.legend()
plt.grid()
plt.savefig(
    "images/particle_in_box_probability.png",
    dpi=300,
    bbox_inches="tight",
)
plt.show()
print("Energy Levels")
for n in [1, 2, 3]:
    energy_joules = energy_level(
        n,
        box_length,
    )
    energy_ev = (
        energy_joules
        / 1.602176634e-19
    )
    print(
        f"n = {n}: "
        f"{energy_ev:.3f} eV"
    )