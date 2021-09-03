import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)  # Create a matrix image ((size, color scale), np.uint8 give values to 0 to 255
# print(img)
# img[200:500, 200:400] = 255, 0, 0  # Paint all img blue [y, x]
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 0, 255), 3)
# This function draws a line on image, (img, start, end, color)

# Another functions: cv2.rectangle and cv2.circle, cv2.FILLED to fill all the shape.
# We also can print texts on the image using cv2.putText (Check time 42:26 of LEARN OPENCV).

cv2.imshow("Image", img)

cv2.waitKey(0)