import cv2
import mediapipe as mp
import time


# using our webcam
cap = cv2.VideoCapture(0)

# related to hand detection module

mpHands = mp.solutions.hands
hands = mpHands.Hands()


# running the webcam itself, infinite loop while True
while True:
    # this gives us our frame
    success, img = cap.read()

    cv2.imshow("Image", img)
    cv2.waitKey(1)
