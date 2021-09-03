import cv2
import numpy as np

path = 'Resources/shapes.png'
img = cv2.imread(path)
imgContour = img.copy()  # Copy the img


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # This will retrieves the
    # external outer contours
    for cnt in contours:
        area = cv2.contourArea(cnt)  # Calculate the area
        print(area)
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)  # As the name says, draw the contours
            peri = cv2.arcLength(cnt, True)  # Perimeter of the shapes
            print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)  # Approximate the number of corners
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)  # Give us the x, y, weight and height for each shape
            cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 2)


# Pre process the image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 150, 200)
getContours(imgCanny)

imgStack = stackImages(0.6, ([img, imgContour], [imgCanny, img]))
cv2.imshow("Stacked", imgStack)
cv2.waitKey(0)
