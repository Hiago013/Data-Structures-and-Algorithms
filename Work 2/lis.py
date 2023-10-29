import numpy as np
class lin_problem(object):
    def __init__(self, arr : list):
        self.__arr = arr
    

    def solve_dynamic_programming(self):
        arr = self.__arr
        n = len(arr)
 
        lis = [1]*n
        solucao = list()
        
        # Compute optimized LIS values in bottom up manner
        for i in range(1, n):
            aux_solucao = list()
            for j in range(0, i):
                if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j]+1
                    aux_solucao.append(arr[j])
            aux_solucao.append(arr[i])
            if len(aux_solucao) > len(solucao):
                solucao = aux_solucao

        return solucao, len(solucao)



# Driver program to test above function
if __name__ == '__main__':
    arr = [45, 18, 21, 28,  5, 32, 14, 19, 23, 30]#np.random.randint(0, 50, 10)#[10, 22, 9, 33, 21, 50, 41, 60]
    solver = lin_problem(arr)
    max_subsequence, length = solver.solve_dynamic_programming()
    print(f'Sequence: {arr}')
    print(f'Max Subquence: {max_subsequence}. Length: {length}')