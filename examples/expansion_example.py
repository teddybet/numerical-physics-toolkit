import numpy as np
import matplotlib.pyplot as plt
from physicspy.cosmology.expansion import hubble_parameter
scale_factors = np.linspace(0.1, 1.0, 200)
hubble_values = [
    hubble_parameter(a)
    for a in scale_factors
]
plt.plot(scale_factors, hubble_values)
plt.xlabel("Scale Factor a")
plt.ylabel("Hubble Parameter H(a) [km/s/Mpc]")
plt.title("Expansion History in a Flat Matter + Dark Energy Universe")
plt.grid()
plt.savefig(
    "images/expansion_history.png",
    dpi=300,
    bbox_inches="tight",
)
plt.show()