import numpy as np
import matplotlib.pyplot as plt
from numpy import log
from matplotlib.animation import FuncAnimation

# y=ln(1+x)


def get_kth_summ(x, k):
    assert(abs(x) <= 1)
    yield x
    summ = x
    prev_values = x
    count = 1
    while count < k:
        prev_values *= x
        prev_values = -prev_values
        summ += prev_values/(count+1)
        count += 1
        yield summ

def create_and_fill_numpy_array(n, x):
    a = np.array([i for i in get_kth_summ(x, n)], dtype=np.float128)


def animate(n):
    y_range = [i for i in range(n)]
    a = np.array([i for i in get_kth_summ(x, n)], dtype=np.float128)
    line.set_data(y_range, a)
    return line



if __name__ == '__main__':
    x = 0.9
    n = 100
    fig = plt.figure()
    a = np.array([i for i in get_kth_summ(x, n)], dtype=np.float128)
    y_range = [i for i in range(n)]
    plt.plot(y_range, [log(1+x) for i in y_range], "--r",label="Справжне значення")
    line, = plt.plot([], [], "-b", lw=1, label="Наближення")
    anim = FuncAnimation(
        fig,            
        animate,         
        frames=100,        
        interval=400,   
        repeat=True      
    )
    plt.legend()
    plt.show()

