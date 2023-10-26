import numpy as np



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
    path = []
    
    for line in range(w):
      for column in range(h):
        if line < w - 1 and column < h - 1:
          table[line, column] = max(self.__grid_world[line + 1, column],\
                                    self.__grid_world[line, column + 1])
        elif line < w - 1:
          table[line, column] = self.__grid_world[line + 1, column]
        elif column < h - 1:
          table[line, column] = self.__grid_world[line, column + 1]
    
    return table

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

          elif x_current < xg - 1:
              path.append(0)
              x_current += 1
          elif y_current < yg - 1:
              path.append(1)
              y_current += 1
      return path

  def solve_backtracking(self):
    global global_path, distance, count
    count = 0
    global_path = []
    distance = -np.inf
    path = [-1 for i in range(self.__xg + self.__yg - 2)]
    self.__helper_backtracking(path)
    print(count)
    return path

  def __helper_backtracking(self, path, S = 0, index_down = 0, index_right = 0, i = 0):
    global global_path, distance, count
    count += 1
    wg, hg = self.__xg, self.__yg
    if (wg - 1, hg - 1) == (index_down, index_right):
        if S > distance:
          global_path = path
          distance = S
    else:
        if index_down < wg - 1 and S != -np.inf:
            path[i] = 0
            self.__helper_backtracking(path, S + self.__grid_world[index_down, index_right], index_down + 1, index_right, i + 1)
        if index_right < hg - 1 and S != -np.inf:
            path[i] = 1
            self.__helper_backtracking(path, S + self.__grid_world[index_down, index_right], index_down, index_right + 1, i + 1)

       
                
if __name__ == "__main__":
    grid_world = create_grid_world((5, 5)) # Create Grid World
    insert_obstacle(grid_world, (2, 1))    # Insert Obstacle
    insert_obstacle(grid_world, (4, 1))    # Insert obstacle

    planner = path_planning(grid_world=grid_world)
    print(planner.solve_greedy())
    print(planner.solve_backtracking())
    print(planner.solve_dynamic_programming())

