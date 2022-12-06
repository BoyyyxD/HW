import numpy as np

def double_check(func):
    def _my_wrapper(arr):
        return func(arr) and func(arr.T)
    return _my_wrapper

@double_check
def check_if_magical(arr):
    l = len(arr[0])
    summa = np.sum(arr[0])
    for i in range(l):
        if summa != np.sum(arr[i]):
            return False
    return True

 


if __name__ == "__main__":
    print(check_if_magical(np.array([[5,5,5],[5,5,5],[5,5,5]])))
    print(check_if_magical(np.array([[5,5,5],[5,8,5],[6,5,5]])))





