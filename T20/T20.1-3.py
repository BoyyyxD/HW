
import numpy as np
import matplotlib.pyplot as plt

# lim = 0.75

def create_and_compute(n):
    a = np.array([0 for i in range(n)], dtype=np.float128)
    k = 0
    for i in range(1, n):
        a[i] = get_element(i)
    return a

def get_k(arr, eps, lim=0.75):
    for i, j in enumerate(arr):
        if abs(j-lim) < eps:
            return i
    return -1


def get_element(k):
    
    bot = (2*(k**2))+5
    top = np.power(k, 1/k)
    top *= (k-3)
    tmp, curr = k, k
    for i in range(1, k+1):
        tmp/=3
        curr += tmp
    return top*curr/bot


def solve():
    return

if __name__ == "__main__":
    const_optimal_value = 20000
    arr = create_and_compute(const_optimal_value)
    lim = 0.75
    eps = 0.0004
    # print(get_k(arr, eps))
    print("lol")
    plt.plot(range(const_optimal_value)[200:], arr[200:])
    plt.plot(range(const_optimal_value)[200:], [lim for i in range(const_optimal_value)][200:])
    plt.plot(range(const_optimal_value)[200:], [lim-eps for i in range(const_optimal_value)][200:])
    plt.plot(range(const_optimal_value)[200:], [lim+eps for i in range(const_optimal_value)][200:])
    plt.show()