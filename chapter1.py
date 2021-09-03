import cv2

print("Package imported")

""""
img = cv2.imread("Resources/boat.jpg")  # Read the image
cv2.imshow("Output", img)  # Show the image, which you put the window name and the variable
cv2.waitKey(0)  # Sets the image display time, in ms
"""

"""
cap = cv2.VideoCapture("Resources/teste 2.mp4")  # This function capture the video

# As a video is made by multiple images, we need a loop to show all the images
while True:
    success, img = cap.read()
    # The images will be saved in img, and success will tell us if this worked, as a boolean variable, true or false
    cv2.imshow("Video", img)
    # This show all images
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        # If we press q, the video will close, if not, the video continues until his end
        break
"""


cap = cv2.VideoCapture(0)  # This function capture the webcam video, as I have one webcam, I'll choose 0
# We can configure how we'll see the image, using .set(number of parameter, value)
cap.set(3, 640)  # Set the webcam width
cap.set(4, 480)  # Set the webcam height
cap.set(10, 100)  # Set the webcam brightness

# As a video is made by multiple images, we need a loop to show all the images
while True:
    success, img = cap.read()
    # The images will be saved in img, and success will tell us if this worked, as a boolean variable, true or false
    cv2.imshow("Video", img)
    # This show all images
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # If we press q, the video will close, if not, the video continues until his end
        break
