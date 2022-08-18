# GESTURE VOLUME CONTROL
# first using handtracking, then use hand landmarks to find the gesture of our hands, we will use the handtracking module.

# 1. importing cv2, time, and numpy after installing on pip
import cv2
import time
import numpy as np

from HandTracking import HandTrackingModule as htm

#################################################

wCam, hCam = 640, 480
#################################################

# 2. check if webcam is working, VideoCapture(0) is normally laptop camera
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.75)


while True:
    # 3. checking the success of the camera capturing any image
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw = False)
    

    # we need landmark values 4 and 8 for our thumb point and index point
    if len(lmList) != 0:
        print(lmList[4], lmList[8])
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]

        # getting the center of the line
        cx, cy  =  (x1 + x2) //2, (y1+y2) // 2

        # making the landmarks on the tip of the thumb in index tip bigger
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        
        # creating a line between the thumb and the index finger
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

        # cirle for center of line between thumb and index
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f"FPS: {int(fps)}", (40, 50), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    
    
    
    # 4. 
    cv2.imshow("Img", img)
    cv2.waitKey(1)
    