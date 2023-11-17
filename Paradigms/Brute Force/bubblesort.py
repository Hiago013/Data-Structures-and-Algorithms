def bubble_sort(unsorted_list):
    L = len(unsorted_list)
    for i in range(0, L - 1):
        for j in range(0, L - i - 1):
            if unsorted_list[j] > unsorted_list[j+1]:
                aux = unsorted_list[j]
                unsorted_list[j] = unsorted_list[j+1]
                unsorted_list[j+1] = aux
    
    sorted_list = unsorted_list
    return sorted_list

A = [1,25,457,571,0,-5,5]
print(A)
print(bubble_sort(A))
