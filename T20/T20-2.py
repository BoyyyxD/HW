import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def get_circle_arr():
    x1 = np.linspace(-1, 1, 1000)
    x2 = np.linspace(1, -1, 1000)
    y1 = -np.sqrt(1 - x1 * x1)
    y2 = np.sqrt(1 - x2 * x2)
    return np.hstack((x1, x2)), np.hstack((y1, y2))


def get_corrcet_n_angle(n):
    x = np.array([np.cos(i * 2 * np.pi / n) for i in range(n + 1)])
    y = np.array([np.sin(i * 2 * np.pi / n) for i in range(n + 1)])
    return x, y


# def get_perimeter(x, y):
#     return np.sqrt((x[0] - x[1]) ** 2 + (y[0] - y[1]) ** 2) * (x.size - 1)

def animate(i):
    x, y = get_corrcet_n_angle(2 ** (i + 2))
    line.set_data(x, y)
    return line


if __name__ == "__main__":
    fig = plt.figure()
    plt.axes(xlim=(-2, 2), ylim=(-1.5, 1.5))
    plt.plot(*get_circle_arr(), "--r", lw=2, label="Коло")
    line, = plt.plot([], [], "-b", lw=1, label="Наближення")
    anim = FuncAnimation(
        fig,  # Полотно, на якому буде зображено анімацію
        animate,  # Функція для анімації
        frames=60,  # Кількість ітерацій анімації (починається з 0)
        interval=1000,  # Кількість мілісекунд на ітерацію
        repeat=True  # Чи повторювати анімацію після останньої ітерації
    )
    plt.legend()
    plt.show()