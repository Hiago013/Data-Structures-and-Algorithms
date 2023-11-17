from numpy import infty
def MSS(lista):
    max_sum = -infty
    L = len(lista)
    for i in range(0, L):
        aux_sum = 0
        for j in range(i, L):
            aux_sum += lista[j]
            if aux_sum > max_sum:
                max_sum = aux_sum
                I = i
                J = j
    return I, J, max_sum

X = [-2, 11, -4, 13, -5, 2]
print(MSS(X))