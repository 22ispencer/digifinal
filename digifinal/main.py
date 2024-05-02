import math
import matplotlib.pyplot as plt
import numpy as np
import random

SIZE = 500


def generate_balls(count: int, radius: float) -> np.ndarray:
    rad_int = math.ceil(radius)
    x = np.random.randint(rad_int, SIZE - rad_int, [count])
    y = np.zeros(count)
    v = np.random.randint(0, 3, [count])

    for i, x_0 in enumerate(x):
        max = bound_func(x_0, radius)
        y[i] = random.randint(math.ceil(radius), int(max))
        while 1 in collide_check(np.array([x, y]), radius)[i]:
            y[i] = random.randint(0, int(max))

    return np.array([x, y, v])


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


def draw():
    fig, ax = plt.subplots()

    count = 10
    radius = 5

    while plt.fignum_exists(fig.number):  # type: ignore
        # Reset plot
        ax.cla()

        # Plot boundaries
        ax.plot([0, SIZE / 2], [SIZE / 2, SIZE], "b")
        ax.plot([SIZE / 2, SIZE], [SIZE, SIZE / 2], "b")
        ax.set_xlim(left=0, right=500)
        ax.set_ylim(top=500, bottom=0)

        # Plot Balls
        balls = generate_balls(count, radius)
        ax.plot(balls[0], balls[1], "bo", markersize=radius)

        # Show graph
        plt.pause(0.016667)


def run():
    draw()
