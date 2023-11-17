def selection_sort(unsorted_list):
    L = len(unsorted_list)
    start = 0
    for i in range(0, L - 1):
        start += 1
        for j in range(start, L):
            if unsorted_list[j] < unsorted_list[i]:
                 aux = unsorted_list[j]
                 unsorted_list[j] = unsorted_list[i]
                 unsorted_list[i] = aux
    
    sorted_list = unsorted_list
    return sorted_list


A = [1,25,457,571,0,-5,5]
print(A)
print(selection_sort(A))
