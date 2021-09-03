import cv2
import numpy as np

# Import the image and read it.
img = cv2.imread("Resources/boat.jpg")
# Define Kernel. (Kernel is a matrix which works as a filter to the image, for better interpretation for system.
kernel = np.ones((5, 5), np.uint8)  # Means that we want all of the values to be 1


imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# This put a filter on the image, which turns the image in grey scale

imgBlur = cv2.GaussianBlur(img, (7, 7), 0)
# This put a blur on the image,(image, (kernel size), sigma x)

imgCanny = cv2.Canny(img, 150, 200)
# This put a filter which shows the edges of the picture, like a edge detector

# Unfortunately, this filter may not recognize a line of the image as being just one line, but several, so we'll use
# another filter


# Dilation makes the lines more thickness
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
# We'll work with edges, so image var will be canny (img, kernel size, iterations (we can define how much thickness
# we need)

# Erosion makes the opposite of Dilation, it makes the lines thinner
imgEroded = cv2.erode(imgDilation,kernel, iterations=3)

while True:
    cv2.imshow("Original", img)
    cv2.imshow("Blur", imgBlur)
    cv2.imshow("Canny", imgCanny)
    cv2.imshow("Dilation", imgDilation)
    cv2.imshow("Eroded", imgEroded)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
