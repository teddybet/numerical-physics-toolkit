import matplotlib.pyplot as plt
from physicspy.mechanics.orbit import simulate_orbit
SUN_MASS = 1.989e30
initial_position = [1.496e11, 0]
initial_velocity = [0, 29_780]
time_step = 3600
total_time = 365.25 * 24 * 3600
times, positions = simulate_orbit(
    initial_position=initial_position,
    initial_velocity=initial_velocity,
    central_mass=SUN_MASS,
    time_step=time_step,
    total_time=total_time,
)
x = positions[:, 0]
y = positions[:, 1]
plt.plot(x, y)
plt.scatter(0, 0, label="Sun")
plt.xlabel("x position (m)")
plt.ylabel("y position (m)")
plt.title("Planetary Orbit")
plt.axis("equal")
plt.grid()
plt.legend()
plt.savefig(
    "images/orbit.png",
    dpi=300,
    bbox_inches="tight",
)
plt.show()