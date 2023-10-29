# Our Setup, Import Libaries, Create our Imshow Function and Download our Images
import cv2
import numpy as np
from matplotlib import pyplot as plt

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
    cv2.circle(image, (w - w_step // 2 , h // 2), w_step // 4, (0,0,0), -1)
    cv2.circle(image, (w // 2 , h - h_step//2), w_step // 4, (0,0,0), -1)

# Create a white image using numpy to create and array of white
image = 255 * np.ones((512,512,3), np.uint8)

draw_robot((5,5), image)
draw_goal((5,5), image)
draw_grid_world((5, 5), image = image)
draw_obstacle((5,5), image)
draw_path((5,5), image, [0, 0, 1, 1, 0, 1, 0, 1])
draw_path((5,5), image, [1, 1, 0, 0, 1, 0, 1, 0], [250, 150, 0])
draw_path((5,5), image, [0, 0, 0, 0, 1], [250, 0, 150])

imshow("Grid World", image)