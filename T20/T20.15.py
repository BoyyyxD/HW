import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

x_coords = [1, 2, 3, 4]
y_coords = [5, 6, 7, 8]

def get_3d_matrics(arr):
    n = len(arr[0])
    arr = np.rot90(arr, k=1, axes=(0, 1))

    size_3d = int(n*(n-1)*(n-2)/6)
    array_3d = np.zeros((size_3d, 3, 2))
    cnt = 0
    for x in range(n-2):
        for y in range(x+1, n-1):
            for z in range(y+1, n):
                array_3d[cnt] = [arr[x], arr[y], arr[z]]
                cnt += 1
    return array_3d

def has_equal_sides(array_2d):
    dis1= (array_2d[0] - array_2d[1])**2
    dis2= (array_2d[0] - array_2d[2])**2
    dis3= (array_2d[1] - array_2d[2])**2
    print(dis1)
    print(dis2)
    print(dis3)
    return sqrt(np.sum(dis1)) == sqrt(np.sum(dis2)) == sqrt(np.sum(dis3))   






if __name__ == "__main__":
    arr = np.array([x_coords, y_coords])
    arr_3d = get_3d_matrics(arr)
    print(np.rot90(arr_3d[0], k=1, axes=(0, 1)))
    for i in arr_3d:
        if has_equal_sides(arr_3d[i]):
            print(arr_3d[i])