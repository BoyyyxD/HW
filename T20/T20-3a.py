import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def get_sin_at_x(x, n):
    sin = x.copy()
    tmp = x.copy()
    for i in range(2, n + 1):
        tmp *= -x*x / ((2*i - 2)*(2*i - 1))
        sin += tmp
    return sin


def plot_sin():
    plt.plot(x, np.sin(x), "r", label="sin (x)")
    return line


def animate(i):
    y = get_sin_at_x(x, i + 1)
    line.set_data(x, y)
    return line


if __name__ == "__main__":

    st, en, m = -4*np.pi, 4*np.pi, 20  # Початок 
    x = np.linspace(st, en, int((en - st) * 50))
    fig = plt.figure('b')
    # Змінюємо масштаб осей
    plt.axes(xlim=(st, en), ylim=(-5, 5))
    # Створємо пустий графік і надаємо йому параметри відображення
    line, = plt.plot([], [], "--b", label="Наближення",lw=3)
    anim = FuncAnimation(
        fig,            
        animate,         
        init_func=plot_sin,  
        frames=m,        
        interval=700,   
        repeat=True      
    )
    plt.legend()
    plt.show()