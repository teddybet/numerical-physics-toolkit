import matplotlib.pyplot as plt
from physicspy.mechanics.projectile import (
    projectile_motion,
    projectile_statistics,
)
times, x, y = projectile_motion(
    initial_speed=30,
    angle_degrees=45,
)
maximum_height, flight_time, horizontal_range = projectile_statistics(
    initial_speed=30,
    angle_degrees=45,
)
print(f"Maximum Height: {maximum_height:.2f} m")
print(f"Flight Time: {flight_time:.2f} s")
print(f"Horizontal Range: {horizontal_range:.2f} m")
plt.plot(x, y)
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Height (m)")
plt.title("Projectile Motion")
plt.grid()
plt.savefig(
    "images/projectile_motion.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()