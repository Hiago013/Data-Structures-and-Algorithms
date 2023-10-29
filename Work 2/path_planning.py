import numpy as np
from tree_node import TreeNode 
import graphviz

# Visualize a binary tree using Graphviz
def visualize_binary_tree(root):
    dot = graphviz.Digraph()
    dot.node(str(root.key))

    def add_nodes_edges(node):
        if node.left:
            dot.node(str(node.left.key))
            dot.edge(str(node.key), str(node.left.key))
            add_nodes_edges(node.left)  # Recursively add left child nodes
        if node.right:
            dot.node(str(node.right.key))
            dot.edge(str(node.key), str(node.right.key))
            add_nodes_edges(node.right)  # Recursively add right child nodes

    add_nodes_edges(root)
    dot.render('binary_tree', view=True, format='png')  # Render and display the binary tree

# Create a grid world of a specified size
def create_grid_world(size):
    width, height = size
    grid_world = np.zeros((width, height))
    for row in range(width):
        for col in range(height):
            grid_world[row, col] = -((width - row - 1) + (height - col - 1))
            # Fill the grid with values based on position

    return grid_world

# Insert an obstacle at a specific position in the grid world
def insert_obstacle(grid_world, obstacle_position):
    width, height = grid_world.shape[0], grid_world.shape[1]
    obs_x, obs_y = obstacle_position
    grid_world[obs_x, obs_y] = -np.inf  # Set the obstacle position to negative infinity
    for row in range(max(0, obs_x - 1), min(width, obs_x + 2)):
        for col in range(max(0, obs_y - 1), min(height, obs_y + 2)):
            grid_world[row, col] -= 1  # Decrease values in the neighboring cells

class PathPlanning(object):
  PATHS =           {'greedy': {'path': [], 'basic_operation': 0},
               'backtracking': {'path': [], 'basic_operation': 0},
        'dynamic_programming': {'path': [], 'basic_operation': 0}}
  def __init__(self, grid_world):
    self.__grid_world = grid_world
    self.__xg, self.__yg = self.__grid_world.shape
  
  def solve_dynamic_programming(self):
    self.PATHS['dynamic_programming']['basic_operation'] = 0
    width, height = self.__xg, self.__yg

    # Create and initialize the table for dynamic programming
    table = np.zeros((width, height))
    table[0, 0] = self.__grid_world[0, 0]

    # Fill in the table using dynamic programming
    for column in range(1, height):
        table[0, column] = table[0, column - 1] + self.__grid_world[0, column]
    for line in range(1, width):
        table[line, 0] = table[line - 1, 0] + self.__grid_world[line, 0]
        for column in range(1, height):
            table[line, column] = np.max([table[line - 1, column], table[line, column - 1]]) + self.__grid_world[line, column]
            self.PATHS['dynamic_programming']['basic_operation'] += 1

    # Find the optimal path using the helper function
    path = self.__helper_dynamic_programming(table, width - 1, height - 1)

    # Update the path in the PATHS dictionary
    self.PATHS['dynamic_programming']['path'] = path

    return path


  def solve_greedy(self):
    self.PATHS['greedy']['basic_operation'] = 0
    path = []
    x_current, y_current = (0, 0)
    xg, yg = self.__xg, self.__yg

    # Continue until the bottom-right corner is reached
    while (xg - 1, yg - 1) != (x_current, y_current):
        self.PATHS['greedy']['basic_operation'] += 1

        if x_current < xg - 1 and y_current < yg - 1:
            # Choose the action with the highest grid value
            action = np.argmax([self.__grid_world[x_current + 1, y_current],
                                self.__grid_world[x_current, y_current + 1]])
            path.append(action)
            if action == 0:
                x_current += 1
            else:
                y_current += 1
        elif x_current < xg - 1 and self.__grid_world[x_current + 1, y_current] != -np.inf:
            path.append(0)
            x_current += 1
        elif y_current < yg - 1 and self.__grid_world[x_current, y_current + 1] != -np.inf:
            path.append(1)
            y_current += 1
        else:
            print("Impossible to solve!")
            self.PATHS['greedy']['path'] = path
            return -1

    self.PATHS['greedy']['path'] = path
    return path


  def solve_backtracking(self):
    global global_path, distance, count
    self.PATHS['backtracking']['basic_operation'] = 0
    count = 0
    global_path = []
    distance = -np.inf

    # Create a path list with -1 values
    path = [-1 for _ in range(self.__xg + self.__yg - 2)]

    # Create the root of the decision tree
    decision_tree = TreeNode('root')

    # Start the backtracking algorithm to find the optimal path
    self.__helper_backtracking(decision_tree, path, self.__grid_world[0, 0])

    # Optionally visualize the decision tree
    # visualize_binary_tree(decision_tree)

    # Update the backtracking path in the PATHS dictionary
    self.PATHS['backtracking']['path'] = global_path

    return global_path


  def __helper_backtracking(self, tree: TreeNode, path, S=0, index_down=0, index_right=0, i=0):
    global global_path, distance, count
    count += 1
    self.PATHS['backtracking']['basic_operation'] += 1
    width_grid, height_grid = self.__xg, self.__yg

    # Check if we have reached the bottom-right corner of the grid
    if (width_grid - 1, height_grid - 1) == (index_down, index_right):
        if S > distance:
            global_path = np.copy(path)
            distance = S
    else:
        if index_down < width_grid - 1 and S != -np.inf:
            # Explore the path by moving down
            tree.left = TreeNode(f'Down {count}')
            path[i] = 0
            self.__helper_backtracking(tree.left, path, S + self.__grid_world[index_down + 1, index_right], index_down + 1, index_right, i + 1)
        if index_right < height_grid - 1 and S != -np.inf:
            # Explore the path by moving right
            tree.right = TreeNode(f'Right {count}')
            path[i] = 1
            self.__helper_backtracking(tree.right, path, S + self.__grid_world[index_down, index_right + 1], index_down, index_right + 1, i + 1)


  def __helper_dynamic_programming(self, table, index_down=0, index_right=0, path=[]):
      # Base case: Reached the top-left corner of the grid
      if (0, 0) == (index_down, index_right):
          return path
      else:
          if 0 < index_down and 0 < index_right:
              # Determine the optimal action based on the table values
              action = np.argmax([table[index_down - 1, index_right],
                                  table[index_down, index_right - 1]])
          elif 0 < index_down:
              action = 0
          elif 0 < index_right:
              action = 1

          # Recursively explore the path by adding the chosen action to the path
          if action == 0:
              path_ok = self.__helper_dynamic_programming(table,
                                                        index_down=index_down - 1,
                                                        index_right=index_right,
                                                        path=[0] + path)
          else:
              path_ok = self.__helper_dynamic_programming(table,
                                                        index_down=index_down,
                                                        index_right=index_right - 1,
                                                        path=[1] + path)
      return path_ok
                
if __name__ == "__main__":
    grid_world = create_grid_world((5, 5)) # Create Grid World
    insert_obstacle(grid_world, (0, 1))    # Insert Obstacle
    insert_obstacle(grid_world, (2, 0))    # Insert Obstacle

    print(grid_world)
    planner = PathPlanning(grid_world=grid_world)
    print('Greedy -- >', planner.solve_greedy())
    print('BackTracking -- >', planner.solve_backtracking())
    print('DynamicPrograming -- >', planner.solve_dynamic_programming())

