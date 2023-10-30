from path_planning import PathPlanning, create_grid_world, insert_obstacle
from view import View
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn')

SMALL_SIZE = 16
MEDIUM_SIZE = 16
BIGGER_SIZE = 16

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE) 


def main(grid_size):
    # Create the grid world
    w, h = grid_size
    grid_world = create_grid_world(grid_size)
    insert_obstacle(grid_world, (w - 2, h // 2))
    
    print(grid_world)

    # Initialize the path planner
    planner = PathPlanning(grid_world)

    # Solve using different algorithms
    planner.solve_greedy()
    planner.solve_backtracking()
    planner.solve_dynamic_programming()

    # Initialize the viewer
    viewer = View(grid_size, 255 * np.ones((512, 512, 3), np.uint8))
    
    # Draw elements on the viewer
    viewer.draw_robot()
    viewer.draw_goal()
    viewer.draw_grid_world()
    viewer.draw_obstacle([(w // 2, h - 2)])
    viewer.draw_path(planner.PATHS['backtracking']['path'], color=[250, 150, 0])
    viewer.draw_path(planner.PATHS['greedy']['path'], color=[0, 150, 250])
    viewer.draw_path(planner.PATHS['dynamic_programming']['path'], color=[150, 0, 250])

    return planner.PATHS

if __name__ == "__main__":
    init, end = 3, 11
    GL = np.zeros(end - init )
    BT = np.zeros(end - init )
    OT = np.zeros(end - init )
    for i in range(init, end):
        print(i, end='-->')
        paths = main((i, i))
        GL[i - init] = paths['greedy']['basic_operation']
        BT[i - init] = paths['backtracking']['basic_operation']
        OT[i - init] = paths['dynamic_programming']['basic_operation']
        print('\n')

    plt.plot(GL)
    plt.plot(OT)
   # plt.plot(BT)
    plt.legend(['Gulosa', 'Programação Dinâmica'])
    plt.xlabel("Tamanho da Entrada (n, n)")
    plt.ylabel("# Operação Básica")
    plt.tight_layout()
    plt.savefig("Figure_5.png", dpi = 600)
    plt.show()