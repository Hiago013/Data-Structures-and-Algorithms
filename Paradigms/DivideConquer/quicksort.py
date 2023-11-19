def partition(L, low, high):
            pivot = L[high] # Choose the last element as the pivot
            j = low - 1   # Index of smaller element
            for i in range(low, high + 1):
                if L[i] <= pivot:
                    j += 1
                    if i > j:
                        L[i], L[j] = L[j], L[i]
            return j

def quicksort_helper(L, low, high):
     if low < high:
          pivot_idx = partition(L, low, high)
          print(L)
          quicksort_helper(L, low, pivot_idx - 1)
          quicksort_helper(L, pivot_idx + 1, high)

def quicksort(L):
    low = 0
    high = len(L) - 1
    quicksort_helper(L, low, high)


L = [3, 2, 5, 0, 1, 8, 7, 6, 9, 4]
print(L, 'first')

quicksort(L)
print(L)


