import cv2
import numpy as np

# path
path = 'cat.jpg'

# Reading an image in default
# mode
image = cv2.imread(path)

# Window name in which image is
# displayed
window_name = 'Image'

# Polygon corner points coordinates
pts = np.array([[500, 3], [500, 160],
                [400, 100]],
               np.int32)

pts = pts.reshape((-1, 1, 2))

isClosed = True

# Blue color in BGR
color = (255, 0, 0)

# Line thickness of 2 px
thickness = 2

# Using cv2.polylines() method
# Draw a Blue polygon with
# thickness of 1 px
image = cv2.polylines(image, [pts],
                      isClosed, color, thickness)

image = cv2.circle(image, (250, 250), 35, [255, 0, 255], 2)
#image = cv2.tr #.circle(image, (250, 250), 35, [255, 0, 255], 2)

# Displaying the image

cv2.imshow('image', image)
cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imwrite("cat_1.jpg", image)