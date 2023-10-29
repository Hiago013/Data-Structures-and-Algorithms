from path_planning import path_planning,\
                          create_grid_world, insert_obstacle

from multiprocessing import Process

def main(grid_size):
    w, h = grid_size
    grid_world = create_grid_world(grid_size)
    insert_obstacle(grid_world, (w//2, h-1))
    insert_obstacle(grid_world, (w - 1, h // 2))
    #insert_obstacle(grid_world, (w//2, 0))
    
    print(grid_world)

    planner = path_planning(grid_world)

    t1 = Process(target=planner.solve_greedy)
    t2 = Process(target=planner.solve_backtracking)
    t3 = Process(target=planner.solve_dynamic_programming)
    t1.start()
    t2.start()
    t3.start()

    print(grid_world)
    #print('Greedy -- >', planner.solve_greedy(), '\n')
    #print('BackTracking -- >', planner.solve_backtracking(), '\n')
    #print('DynamicPrograming -- >', planner.solve_dynamic_programming())



main((7, 7))



