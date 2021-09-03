import cv2
import numpy as np

img = cv2.imread("Resources/boat.jpg")
print(img.shape)  # Used to print values of image size

imgResize = cv2.resize(img, (512, 343))  # Function to resize the image (val, (x, y)
print(imgResize.shape)

# To crop the image we don't need to use a cv function [starting point y, starting point x]
imgCrop = img[0:500, 200:800]

while True:
    cv2.imshow("Image", img)
    cv2.imshow("Resized", imgResize)
    cv2.imshow("Cropped", imgCrop)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
