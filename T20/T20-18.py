import numpy as np
import numpy.random as rnd
import sys

def get_winning_probability(n):
    assert n > 0
    arr = rnd.randint(1,7, size=(n,4))
    arr = arr.sum(axis=1)
    cnt = len(arr[arr<=9])
    return cnt

if __name__ == "__main__":
    assert(len(sys.argv)==2)
    number = int(sys.argv[1])
    p = get_winning_probability(number)
    won_money = p * 10 - number
    print(won_money)
    print("Гра не є чесною")
