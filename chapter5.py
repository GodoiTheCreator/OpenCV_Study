import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")
print(img.shape)

#  cv2.line(img, (302, 236), (370, 350), (255, 0, 0), 2)
#  cv2.line(img, (475, 130), (546, 245), (0, 255, 0), 2)

width, height = 250, 350
pts1 = np.float32([[302, 236], [370, 350], [475, 130], [546, 245]])  # The 4 points of a card on card.jpg
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])  # Points of the same card in other perspective
matrix = cv2.getPerspectiveTransform(pts1, pts2)  # This function transform you matrix perspective based on your points
imgOutput = cv2.warpPerspective(img, matrix, (width, height))  # Gets the warp perspective to the matrix

cv2.imshow("Original", img)
cv2.imshow("Warp", imgOutput)

cv2.waitKey(0)