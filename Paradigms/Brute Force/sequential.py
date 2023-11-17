from time import time
import numpy as np
def search(A, value):
    L = len(A)
    for i in range(0, L):
        if value == A[i]:
            return i
    return -1

def improved_search(A : list, value:float):
    A.append(value)
    i = 0
    while A[i] != value:
        i = i + 1
    return i

A = [np.random.randint(0, 100, 1) for i in range(10000)]
init = time()
print(search(A, 5), (time() - init)*1000)
init = time()
print(improved_search(A, 5), (time() - init)*1000)