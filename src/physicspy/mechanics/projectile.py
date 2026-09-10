import numpy as np
def projectile_motion(
    initial_speed,
    angle_degrees,
    initial_height=0.0,
    gravity=9.81,
    time_step=0.01,
):
    angle_radians = np.radians(angle_degrees)
    velocity_x = initial_speed * np.cos(angle_radians)
    velocity_y = initial_speed * np.sin(angle_radians)
    times = []
    x_positions = []
    y_positions = []
    time = 0.0
    while True:
        x = velocity_x * time
        y = (
            initial_height
            + velocity_y * time
            - 0.5 * gravity * time**2
        )
        if y < 0:
            break
        times.append(time)
        x_positions.append(x)
        y_positions.append(y)
        time += time_step
    return (
        np.array(times),
        np.array(x_positions),
        np.array(y_positions),
    )
def projectile_statistics(
    initial_speed,
    angle_degrees,
    initial_height=0.0,
    gravity=9.81,
):
    angle_radians = np.radians(angle_degrees)
    velocity_x = initial_speed * np.cos(angle_radians)
    velocity_y = initial_speed * np.sin(angle_radians)
    flight_time = (
        velocity_y
        + np.sqrt(velocity_y**2 + 2 * gravity * initial_height)
    ) / gravity
    horizontal_range = velocity_x * flight_time
    maximum_height = (
        initial_height
        + velocity_y**2 / (2 * gravity)
    )
    return maximum_height, flight_time, horizontal_range