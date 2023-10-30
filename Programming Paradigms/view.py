import cv2
import numpy as np
from matplotlib import pyplot as plt

class View(object):
    def __init__(self, size, image):
        self.__image = image
        self.__size = size
    
    def draw_robot(self):
        image_width, image_height = self.__image.shape[0], self.__image.shape[1]
        step_x = image_width // self.__size[0]
        step_y = image_height // self.__size[1]

        # Calculate the center coordinates for the robot
        x_center = step_x // 2
        y_center = step_y // 2
        radius = step_x // 4

        # Draw the robot circle
        cv2.circle(self.__image, (x_center, y_center), radius, (15, 50, 150), -1)

    
    def draw_goal(self):
        image_width, image_height = self.__image.shape[0], self.__image.shape[1]
        step_x = image_width // self.__size[0]
        step_y = image_height // self.__size[1]

        # Calculate the center coordinates for the goal
        x_center = image_width - step_x // 2
        y_center = image_height - step_y // 2
        radius = step_x // 4

        # Draw the goal circle
        cv2.circle(self.__image, (x_center, y_center), radius, (15, 150, 50), -1)

    
    def draw_grid_world(self):
        image_width, image_height = self.__image.shape[0], self.__image.shape[1]
        step_x = image_width // self.__size[0]
        step_y = image_height // self.__size[1]
        
        # Draw the outer rectangle
        cv2.rectangle(self.__image, (0, 0), (image_width, image_height), (127, 50, 127), 10)

        # Draw vertical lines
        for ws in range(self.__size[0] + 1):
            x_position = int(step_x * ws)
            cv2.line(self.__image, (x_position, 0), (x_position, image_height), (127, 50, 127), 5)

        # Draw horizontal lines
        for hs in range(self.__size[1] + 1):
            y_position = int(step_y * hs)
            cv2.line(self.__image, (0, y_position), (image_width, y_position), (127, 50, 127), 5)

    
    def draw_obstacle(self, list_obstacles=[]):
        if len(list_obstacles) > 0:
            image_width, image_height = self.__image.shape[0], self.__image.shape[1]
            step_x = image_width // self.__size[0]
            step_y = image_height // self.__size[1]

            for obstacle in list_obstacles:
                row_obstacle, col_obstacle = obstacle
                x_center = (row_obstacle) * step_x + step_x // 2
                y_center = (col_obstacle) * step_y + step_y // 2
                radius = step_x // 4
                cv2.circle(self.__image, (x_center, y_center), radius, (0, 0, 0), -1)

    
    def draw_path(self, path, color=[150, 150, 150]):
        image_width, image_height = self.__image.shape[0], self.__image.shape[1]
        step_x = image_width // (2 * self.__size[0])
        step_y = image_height // (self.__size[1] * 2)

        # Create points
        points = [[step_x, step_y]]
        i = 1
        j = 1
        for action in path:
            if action == 1:
                i += 2
                points.append([step_x * i, step_y * j])
            else:
                j += 2
                points.append([step_x * i, step_y * j])

        points = np.array(points).reshape((-1, 1, 2))
        cv2.polylines(self.__image, [points], False, color, 3)

    
    def imshow(self, title = "Grid World", size=10):
        w, h = self.__image.shape[0], self.__image.shape[1]
        aspect_ratio = w/h
        plt.figure(figsize=(size * aspect_ratio,size))
        plt.imshow(cv2.cvtColor(self.__image, cv2.COLOR_BGR2RGB))
        plt.title(title)
        plt.show()