import numpy as np
from tree_node import tree_node
import graphviz

def visualize_binary_tree(root):
    dot = graphviz.Digraph()
    dot.node(str(root.key))

    def add_nodes_edges(node):
        if node.left:
            dot.node(str(node.left.key))
            dot.edge(str(node.key), str(node.left.key))
            add_nodes_edges(node.left)
        if node.right:
            dot.node(str(node.right.key))
            dot.edge(str(node.key), str(node.right.key))
            add_nodes_edges(node.right)

    add_nodes_edges(root)
    dot.render('binary_tree', view=True, format='png')

def create_grid_world(size):
  w, h = size
  grid_world = np.zeros((w, h))
  for row in range(w):
    for col in range(h):
      grid_world[row, col] = -((w - row - 1) + (h - col - 1))
  return grid_world

def insert_obstacle(grid_world, obstacle_position):
  w, h = grid_world.shape[0], grid_world.shape[1]
  wo, ho = obstacle_position
  grid_world[wo, ho] = -np.inf
  for row in range(max(0, wo - 1), min(w, wo + 2)):
    for col in range(max(0, ho - 1), min(h, ho + 2)):
      grid_world[row, col] -= 1

class path_planning(object):
  def __init__(self, grid_world):
    self.__grid_world = grid_world
    self.__xg, self.__yg = self.__grid_world.shape
  
  def solve_dynamic_programming(self):
    w, h = self.__xg, self.__yg
    table = np.zeros((w,h))
    table[0, 0] = self.__grid_world[0, 0]


    for column in range(1, h):
       table[0, column] = table[0, column - 1] + self.__grid_world[0, column]
    for line in range(1, w):
      table[line, 0] = table[line-1, 0] + self.__grid_world[line, 0]
      for column in range(1, h):
         table[line, column] = np.max([table[line - 1, column],\
                                    table[line, column - 1]]) + self.__grid_world[line, column]
    path = self.__helper_dynamic_programming(table, w-1, h-1)
    print(path)
    print('table\n', table)
    return path

  def solve_greedy(self):
      path = []
      x_current, y_current = (0, 0)
      xg, yg = self.__xg, self.__yg
      while (xg - 1, yg - 1) != (x_current, y_current):
          if x_current < xg - 1 and y_current < yg -1:
              action = np.argmax([self.__grid_world[x_current + 1, y_current],\
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
             print(path)
             return path
      print(path)
      return path

  def solve_backtracking(self):
    global global_path, distance, count
    count = 0
    global_path = []
    distance = -np.inf
    path = [-1 for i in range(self.__xg + self.__yg - 2)]
    decision_tree = tree_node('root')
    self.__helper_backtracking(decision_tree, path, self.__grid_world[0,0])
    visualize_binary_tree(decision_tree)
    print(global_path)
    return global_path

  def __helper_backtracking(self, tree : tree_node, path, S = 0, index_down = 0, index_right = 0, i = 0):
    global global_path, distance, count
    count += 1
    wg, hg = self.__xg, self.__yg
    if (wg - 1, hg - 1) == (index_down, index_right):
        if S > distance:
          global_path = np.copy(path)
          distance = S
    else:
        if index_down < wg - 1 and S != -np.inf:
            tree.left = tree_node(f'Down {count}')
            path[i] = 0
            self.__helper_backtracking(tree.left, path, S + self.__grid_world[index_down + 1, index_right], index_down + 1, index_right, i + 1)
        if index_right < hg - 1 and S != -np.inf:
            tree.right = tree_node(f'Right {count}')
            path[i] = 1
            self.__helper_backtracking(tree.right, path, S + self.__grid_world[index_down, index_right + 1], index_down, index_right + 1, i + 1)

  def __helper_dynamic_programming(self, table, index_down = 0, index_right = 0, path = []):
      wg, hg = self.__xg, self.__yg
      if (0, 0) == (index_down, index_right):
         return path
      else:
        if 0 < index_down and 0 < index_right:
          action = np.argmax([table[index_down - 1, index_right],
                              table[index_down, index_right - 1]])
        elif 0 < index_down:
          action = 0
        elif 0 < index_right:
          action = 1
            
        if action == 0:
          path_ok = self.__helper_dynamic_programming(table,index_down = index_down - 1,
                                                          index_right = index_right,
                                                          path = [0] + path )
        else:
          path_ok = self.__helper_dynamic_programming(table,index_down = index_down,
                                                          index_right = index_right - 1,
                                                          path = [1] + path )
      return path_ok
                
if __name__ == "__main__":
    grid_world = create_grid_world((5, 5)) # Create Grid World
    insert_obstacle(grid_world, (0, 1))    # Insert Obstacle
    insert_obstacle(grid_world, (2, 0))    # Insert Obstacle

    print(grid_world)
    planner = path_planning(grid_world=grid_world)
    print('Greedy -- >', planner.solve_greedy())
    print('BackTracking -- >', planner.solve_backtracking())
    print('DynamicPrograming -- >', planner.solve_dynamic_programming())

