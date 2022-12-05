import numpy as np
import matplotlib.pyplot as plt
import math
# lim = e



def get_n_th_term(n):
    assert n > 0
    yield 1+1/n
    curr = 1+1/n
    count = 1
    while count < n:
        curr *= (1+1/n)
        count +=1
        yield curr

def get_m(eps, arr, lim=math.e):
    for i, j in enumerate(arr):
        if abs(lim-j) < eps:
            return i
    return -1


if __name__ == '__main__':
    print("Завдання номер T20.1 з: ")
    # Кількість єлементів у масиві
    n = 20000
    # Епсілон
    eps = 0.005
    # Похибка
    rng = 100
    a = np.array([i for i in get_n_th_term(n)], dtype=np.float128)
    m = get_m(eps, a)
    if m == -1:
        print("Занадто мале n для даної похибки")
    else:
        y_range = [i for i in range(n)][-rng:]
        # plt.plot(y_range, [math.e for i in y_range], label="e")
        plt.plot(y_range, a[-rng:], "orange", label="Послідовність")
        plt.plot(y_range, [math.e + eps for i in y_range], "blue", label="Верхня межа")
        plt.plot(y_range, [math.e - eps for i in y_range], "blue", label="Нижня межа")
        plt.plot(y_range, [math.e for i in y_range], "red", label="e")
        # plt.axhline(math.e, xmin=19995, xmax=20000).set_color("purple")
        plt.axvline(m, 0, 3, label="m", color="darkgreen")
        plt.legend()
        plt.show()
