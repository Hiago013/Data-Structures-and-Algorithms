
from numpy import infty, array


def TravelingSalesman(adjacency_matrix, initial_vertice = 0):
    m, _ = adjacency_matrix.shape
    vertices = []
    for node in range(m):
        if node != initial_vertice:
            vertices.append(node)
    
    solutions = []
    travelig_salesman_helper(vertices, solutions)
    feasibles = []

    for path in solutions:
        aux_feasible = [initial_vertice, path[0]]
        second = path[0]
        sum = adjacency_matrix[initial_vertice, second]
        for i in range(1, len(path)):
            current_node = path[i - 1]
            next_node = path[i]
            sum += adjacency_matrix[current_node, next_node]
            if sum == infty:
                break
            aux_feasible.append(next_node)

        sum += adjacency_matrix[next_node, initial_vertice]
        aux_feasible.append(initial_vertice)
        aux_feasible.append(sum)
        feasibles.append(aux_feasible)
    print(feasibles)


def travelig_salesman_helper(vertices, feasible_solutions:list, i = 0, initial_vertice = 0):
    if i == len(vertices):   	 
        print(vertices)
        feasible_solutions.append(vertices)

    for j in range(i, len(vertices)):
        path = [node for node in vertices]
        path[i], path[j] = path[j], path[i]
        travelig_salesman_helper(path, feasible_solutions, i + 1, initial_vertice)

A = array([[infty, 8, 2, 10],
     [8, infty, 7, 1],
     [2, 7, infty, 5],
     [10, 1, 5, infty]])

TravelingSalesman(A)



