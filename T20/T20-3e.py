import numpy as np
import matplotlib.pyplot as plt
from numpy import log
# y=ln(1+x)


def get_kth_summ(x, k):
    print("a")
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


        


if __name__ == '__main__':
    x = 0.9
    n = 100
    a = np.array([i for i in get_kth_summ(x, n)], dtype=np.float128)
    y_range = [i for i in range(n)]
    plt.plot(y_range, [log(1+x) for i in y_range])
    for i in range(100):
        
        line1 = plt.plot(y_range[i:], a)
        plt.show()
        line1.remove()
    
    plt.show()

