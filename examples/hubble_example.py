import numpy as np
import matplotlib.pyplot as plt
from physicspy.cosmology.hubble import recession_velocity
distances = np.linspace(0, 500, 100)
velocities = [
    recession_velocity(distance)
    for distance in distances
]
plt.plot(distances, velocities)
plt.xlabel("Distance (Mpc)")
plt.ylabel("Recession Velocity (km/s)")
plt.title("Hubble's Law")
plt.grid()
plt.savefig(
    "images/hubble_law.png",
    dpi=300,
    bbox_inches="tight",
)
plt.show()