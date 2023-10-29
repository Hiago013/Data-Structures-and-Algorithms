from path_planning import PathPlanning, create_grid_world, insert_obstacle
from view import View
import numpy as np

def main(grid_size):
    # Create the grid world
    w, h = grid_size
    grid_world = create_grid_world(grid_size)
    insert_obstacle(grid_world, (w // 2, h // 2))
    
    print(grid_world)

    # Initialize the path planner
    planner = PathPlanning(grid_world)

    # Solve using different algorithms
    planner.solve_greedy()
    planner.solve_backtracking()
    planner.solve_dynamic_programming()
    
    # Print results
    print(planner.PATHS['greedy'])
    print(planner.PATHS['backtracking'])
    print(planner.PATHS['dynamic_programming'])

    # Initialize the viewer
    viewer = View(grid_size, 255 * np.ones((512, 512, 3), np.uint8))
    
    # Draw elements on the viewer
    viewer.draw_robot()
    viewer.draw_goal()
    viewer.draw_grid_world()
    viewer.draw_obstacle([(w // 2, h // 2)])
    viewer.draw_path(planner.PATHS['backtracking']['path'], color=[250, 150, 0])
    viewer.draw_path(planner.PATHS['greedy']['path'], color=[0, 150, 250])
    viewer.draw_path(planner.PATHS['dynamic_programming']['path'], color=[150, 0, 250])
    viewer.imshow()

if __name__ == "__main__":
    main((5, 5))
