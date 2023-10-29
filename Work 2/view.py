# Our Setup, Import Libaries, Create our Imshow Function and Download our Images
import cv2
import numpy as np
from matplotlib import pyplot as plt

class view(object):
    def __init__(self, size, image):
        self.__image = image
        self.__size = size
    
    def draw_robot(self):
        w, h = self.__image.shape[0] , self.__image.shape[1]
        w_step, h_step = w // self.__size[0], h // self.__size[1]
        cv2.circle(self.__image, (w_step // 2, h_step // 2), w_step // 4, (15,50,150), -1)
    
    def draw_goal(self):
        w, h = self.__image.shape[0] , self.__image.shape[1]
        w_step, h_step = w // self.__size[0], h // self.__size[1]
        cv2.circle(self.__image, (w - w_step // 2, h - h_step // 2), w_step // 4, (15,150,50), -1)
    
    def draw_grid_world(self):
        w, h = self.__image.shape[0] , self.__image.shape[1]
        w_step, h_step = w // self.__size[0], h // self.__size[1]
        cv2.rectangle(self.__image, (0,0), (w,h), (127,50,127), 10)

        for ws in range(self.__size[0] + 1):
            cv2.line(self.__image, (int(w_step * ws), 0), (int(w_step * ws), h), (127,50,127), 5)

        for hs in range(self.__size[1] + 1):
            cv2.line(self.__image, (0, int(h_step * hs)), (w, int(h_step * hs)), (127,50,127), 5)
    
    def draw_obstacle(self, list_obstacles=[]):
        if len(list_obstacles) > 0:
            w, h = self.__image.shape[0] , self.__image.shape[1]
            w_step, h_step = w // self.__size[0], h // self.__size[1]

            for obstacle in list_obstacles:
                row_obstacle, col_obstacle = obstacle
                cv2.circle(self.__image, ((row_obstacle) * w_step + w_step//2, (col_obstacle) * h_step + h_step//2), w_step // 4, (0,0,0), -1)
    
    def draw_path(self, path, color = [150, 150, 150]):
        w, h = self.__image.shape[0] , self.__image.shape[1]
        ro, co = w // (2 * self.__size[0]), h // (self.__size[1] * 2)

        # create pts
        pts = [[ro, co]]
        i = 1
        j = 1
        for action in path:
            if action == 1:
                i += 2
                pts.append([ ro * i, co * j])
            else:
                j += 2
                pts.append([ro * i, co * j])
        
        pts = np.array(pts).reshape((-1, 1, 2))
        cv2.polylines(self.__image, [pts], False, color, 3)

    
    def imshow(self, title = "Grid World", size=10):
        w, h = self.__image.shape[0], self.__image.shape[1]
        aspect_ratio = w/h
        plt.figure(figsize=(size * aspect_ratio,size))
        plt.imshow(cv2.cvtColor(self.__image, cv2.COLOR_BGR2RGB))
        plt.title(title)
        plt.show()


'''
# Define our imshow function
def imshow(title = "Image", image = None, size = 10):
    w, h = image.shape[0], image.shape[1]
    aspect_ratio = w/h
    plt.figure(figsize=(size * aspect_ratio,size))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()

def draw_grid_world(dimension, title = "Grid World", image = None):
  w, h = image.shape[0] , image.shape[1]
  w_step, h_step = w // dimension[0], h // dimension[1]
  cv2.rectangle(image, (0,0), (w,h), (127,50,127), 10)

  for ws in range(dimension[0] + 1):
      cv2.line(image, (int(w_step * ws), 0), (int(w_step * ws), h), (127,50,127), 5)

  for hs in range(dimension[1] + 1):
      cv2.line(image, (0, int(h_step * hs)), (w, int(h_step * hs)), (127,50,127), 5)

  

def draw_robot(dimension, image):
    w, h = image.shape[0] , image.shape[1]
    w_step, h_step = w // dimension[0], h // dimension[1]
    cv2.circle(image, (w_step // 2, h_step // 2), w_step // 4, (15,50,150), -1)


def draw_goal(dimension, image):
    w, h = image.shape[0] , image.shape[1]
    w_step, h_step = w // dimension[0], h // dimension[1]
    cv2.circle(image, (w - w_step // 2, h - h_step // 2), w_step // 4, (15,150,50), -1)

def draw_path(dimension, image, path, color = [0, 150, 250]):

    w, h = image.shape[0] , image.shape[1]
    w_step, h_step = w // dimension[0], h // dimension[1]
    ro, co = w // (2 * dimension[0]), h // (dimension[1] * 2)

    # create pts
    pts = [[ro, co]]
    i = 1
    j = 1
    for action in path:
        if action == 1:
            i += 2
            pts.append([ ro * i, co * j])
        else:
            j += 2
            pts.append([ro * i, co * j])
    
    pts = np.array(pts).reshape((-1, 1, 2))
    cv2.polylines(image, [pts], False, color, 3)

def draw_obstacle(dimension, image):
    w, h = image.shape[0] , image.shape[1]
    w_step, h_step = w // dimension[0], h // dimension[1]
    if dimension[0] % 2 == 0:
        cv2.circle(image, (w - w_step // 2 , h // 2 - h_step//2), w_step // 4, (0,0,0), -1)
        cv2.circle(image, (w // 2 - w_step // 2, h - h_step//2), w_step // 4, (0,0,0), -1)
    else:
        cv2.circle(image, (w - w_step // 2 , h // 2), w_step // 4, (0,0,0), -1)
        cv2.circle(image, (w // 2 , h - h_step//2), w_step // 4, (0,0,0), -1)


# Create a white image using numpy to create and array of white
image = 255 * np.ones((512,512,3), np.uint8)

size = (5,5)
draw_robot(size, image)
draw_goal(size, image)
draw_grid_world(size, image = image)
draw_obstacle(size, image)
#draw_path(size, image, [0, 0, 1, 1, 0, 1, 0, 1])
#draw_path(size, image, [1, 1, 0, 0, 1, 0, 1, 0], [250, 150, 0])
#draw_path(size, image, [0, 0, 0, 0, 1], [250, 0, 150])

imshow("Grid World", image)
'''
if __name__ == "__main__":
    image = 255 * np.ones((512,512,3), np.uint8)
    viewer = view((5, 5), image)

    viewer.draw_robot()
    viewer.draw_goal()
    viewer.draw_grid_world()
    viewer.draw_obstacle([])
    viewer.draw_path([0, 0, 1, 1])
    viewer.imshow()