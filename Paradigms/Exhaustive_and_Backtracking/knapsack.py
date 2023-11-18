def combination(N:list, P:list, q : int, i : int):
    if i == q:
        P.append(N)
    else:
        left = N.copy()
        right = N.copy()

        left.append(0)
        right.append(1)
        combination(left, P, q, i+1)
        combination(right,P, q, i + 1)

def sumweight(P:list, w:list, v:list, max_wight:float):
    values = []
    for i in range(len(P)):
        total_sum = 0
        left_weight = max_wight
        for j in range(len(P[i])):
            if P[i][j] == 1:
                print(v[j], j)
                total_sum += v[j]
                left_weight -= w[j]
            if left_weight < 0:
                total_sum = -1
                break
        values.append(total_sum)
    return values

def searchmax(values):
    max_value = values[0]
    for i in range(1, len(values)):
        if max_value < values[i]:
            max_idx = i
            max_value = values[i]
    return max_value, max_idx




N = []
P = []
c = N.copy()


combination(N, P, 4, 0)

w = [7, 3, 4, 5]
v = [42, 12, 40, 25]
values = sumweight(P, w, v, 10)
print(values)

max_value, max_idx = searchmax(values)
print(max_idx, max_value)