
import numpy as np

def is_ortonorm(arr):
    for i in range(arr.shape[0]):
        for j in range(arr.shape[0]):
            prod = np.dot(arr[i], arr[j])
            if i == j:
                if np.isclose(prod, 1):
                    return False
                else:
                    if np.isclose(prod, 0):
                        return False
    return True

def is_ortonorm_second_check(arr):

    prod = np.dot(arr, arr.T)
    eye = np.eye(arr.shape[0])

    return np.all(np.isclose(eye, prod))


if __name__ == "__main__":
    
    x = np.eye(3)
    print(x)
    print(is_ortonorm(x))
    print(is_ortonorm_second_check(x))


    y = np.array(
        [[1, 2, 3],
         [3, 2, 1],
         [1, 1, 1]
        ],
        dtype=np.float128
        )
    print(is_ortonorm(y))
    print(is_ortonorm_second_check(y))




