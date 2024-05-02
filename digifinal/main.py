import math
import matplotlib.pyplot as plt
import numpy as np
import random

SIZE = 500


def generate_balls(count: int, radius: int) -> np.ndarray:
    x = np.random.randint(radius, SIZE - radius, [count])
    y = np.zeros(count)
    theta = np.random.random([count]) * np.pi
    v_x = np.sin(theta)
    v_y = np.cos(theta)

    for i, x_0 in enumerate(x):
        max = bound_func(x_0, radius)
        y[i] = random.randint(math.ceil(radius), int(max))
        while 1 in collide_check(np.array([x, y]), radius)[i]:
            y[i] = random.randint(0, int(max))

    return np.array([x, y, v_x, v_y])


def bound_func(x: float, radius: float) -> float:
    if x > SIZE / 2:
        return -1 * x + SIZE * 3 / 2 - radius
    return x + int(SIZE / 2) - radius


def collide_check(balls: np.ndarray, radius: float):
    size = len(balls[0])
    collisions = np.zeros([size, size])
    for i in range(len(balls[0])):
        for j in range(len(balls[0])):
            if i != j:
                collisions[i, j] = (
                    1
                    if (
                        math.sqrt(
                            (balls[0, i] - balls[0, j]) ** 2
                            + (balls[1, i] - balls[1, j]) ** 2
                        )
                    )
                    <= 2 * radius
                    else 0
                )
            else:
                collisions[i, j] = 0
    return collisions


def move(balls: np.ndarray, radius: int, count: int):
    collisions = collide_check(balls, radius)
    balls_copy = balls.copy()
    for i in range(count):
        # Ball collisions
        for j, hit in enumerate(collisions[i]):
            if hit:
                balls[2, i] = -balls_copy[2, j]
                balls[3, i] = -balls_copy[3, j]

        # Left/Right wall collision
        if not (radius < balls[0, i] < SIZE - radius):
            balls[2, i] = -balls[2, i]
        # Bottom Wall Collision
        if not (radius < balls[1, i]):
            balls[3, i] = -balls[3, i]
        # Top (V) wall collision
        if not (balls[1, i] < bound_func(balls[0, i], radius)):
            old_v_x = balls[2, i]
            old_v_y = balls[3, i]
            if balls[0, i] < SIZE / 2:
                balls[2, i] = old_v_y
                balls[3, i] = old_v_x
            else:
                balls[2, i] = -old_v_y
                balls[3, i] = -old_v_x
        balls[0, i] += balls[2, i]
        balls[1, i] += balls[3, i]


def draw():
    fig, ax = plt.subplots()

    count = 10
    radius = 5
    fps = 120

    balls = generate_balls(count, radius)
    while plt.fignum_exists(fig.number):  # type: ignore
        move(balls, radius, count)
        # Reset plot
        ax.cla()

        # Plot boundaries
        ax.plot([0, SIZE / 2], [SIZE / 2, SIZE], "b")
        ax.plot([SIZE / 2, SIZE], [SIZE, SIZE / 2], "b")
        ax.set_xlim(left=0, right=500)
        ax.set_ylim(top=500, bottom=0)

        # Plot Balls
        ax.plot(balls[0], balls[1], "bo", markersize=radius)

        # Show graph
        plt.pause(1 / fps)


def run():
    draw()
