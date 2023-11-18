def subsetsum(w, M):
    totalsum = 0
    n = len(w)

    x = [-1] * n
    for i in range(n):
        totalsum += w[i]
    
    if totalsum < M:
        return -1
    
    
    def subsetsum_backtrack(w, M, x, S, T, i):
        if S == M:
            print(x)
        else:
            if S + T >= M:
                x[i] = 0
                subsetsum_backtrack(w, M, x, S, T - w[i], i + 1)
                if S + w[i] <= M:
                    x[i] = 1
                    subsetsum_backtrack(w, M, x, S + w[i], T - w[i], i + 1)
    
    subsetsum_backtrack(w, M, x, 0, totalsum, 0)


w = [3, 5, 6, 7]
M = 15

subsetsum(w, M)