import numpy as np
def gravitational_acceleration(
    position,
    central_mass,
    gravitational_constant=6.67430e-11,
):
    x, y = position
    r = np.sqrt(x**2 + y**2)
    if r == 0:
        raise ZeroDivisionError(
            "Position cannot be at the center of the central mass."
        )
    factor = -gravitational_constant * central_mass / r**3
    return np.array([
        factor * x,
        factor * y,
    ])
def simulate_orbit(
    initial_position,
    initial_velocity,
    central_mass,
    time_step,
    total_time,
    gravitational_constant=6.67430e-11,
):
    position = np.array(initial_position, dtype=float)
    velocity = np.array(initial_velocity, dtype=float)
    positions = [position.copy()]
    times = [0.0]
    time = 0.0
    while time < total_time:
        acceleration = gravitational_acceleration(
            position,
            central_mass,
            gravitational_constant,
        )
        velocity = velocity + acceleration * time_step
        position = position + velocity * time_step
        time += time_step
        positions.append(position.copy())
        times.append(time)
    return np.array(times), np.array(positions)