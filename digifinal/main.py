import matplotlib.pyplot as plt
import numpy as np
import random

SIZE = 500


def generate_balls(count: int) -> np.ndarray:
    coords = SIZE * np.random.rand(2, count)
    print(coords)

    for i in range(len(coords[1])):
        if coords[1, i] > (max := bound_func(coords[1, i])):
            coords[1, i] = random.randint(0, int(max))

    return coords


def bound_func(x: int) -> float:
    if x > SIZE / 2:
        return -1 * x + SIZE * 3 / 2
    return x + int(SIZE / 2)


def bound_eval(x: np.ndarray):
    return np.ndarray(list(map(bound_func, int(x))))


def draw():
    fig, ax = plt.subplots()
    ax.plot([0, SIZE / 2], [SIZE / 2, SIZE])
    ax.plot([SIZE / 2, SIZE], [SIZE, SIZE / 2])
    ax.set_xlim(left=0, right=500)
    ax.set_ylim(top=500, bottom=0)

    balls = generate_balls(10)
    while plt.fignum_exists(fig.number):  # type: ignore
        ax.plot(balls[0], balls[1], "bo")
        plt.pause(1)


def run():
    draw()
