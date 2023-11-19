def binarysearch(L : list, k : float):
    lower_bound = 0
    upper_bound = len(L) - 1

    while lower_bound <= upper_bound:
        average = ( lower_bound + upper_bound ) // 2
        if L[average] == k:
            return average
        
        elif L[average] < k:
            lower_bound = average + 1
        else:
            upper_bound = average - 1
    return -1

L = [10, 2, 3, 8, 10, 0, 58, 95,25, 9,516, 5,62, 56, 90]
L = sorted(L)
print(L)

print(binarysearch(L, 4))