def gencombinations(N, P:list, i = 0):
    if i == len(N):
        P.append(N)
    else:
        for j in range(i, len(N)):
            path = [value for value in N]
            path[i], path[j] = path[j], path[i]
            gencombinations(path, P, i + 1)

def sumCombinations(C, P):
    values = []
    for i in range(0, len(P)):
        total_sum = 0
        for j in range(len(P[i])):
            job = P[i][j]
            total_sum += C[j][job]
        values.append(total_sum)
    return values

def search(V):
    min_value = V[0]
    for i in range(1, len(V)):
        if min_value > V[i]:
            min_value = V[i]
            min_idx = i
    return min_value, min_idx


P = []
N = [0, 1, 2, 3]
C = [[9, 2, 7, 8],
     [6, 4, 3, 7],
     [5, 8, 1, 8],
     [7, 6, 9, 4]]

gencombinations(N, P, 0)

values = sumCombinations(C, P)

min_value, min_idx = search(values)
print(min_value, min_idx)
print('The combination with the smallest sum is: ',P[min_idx], min_value)