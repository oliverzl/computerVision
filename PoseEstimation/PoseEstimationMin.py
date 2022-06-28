# opencv: image processing
# mediapipe: pose estimation

import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture('PoseVideos/1.mp4')
pTime = 0

while True:
    success, img = cap.read()
    cv2.imshow("Image", img)

    # check framerate
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)


    cv2.waitKey(1)