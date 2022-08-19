# GESTURE VOLUME CONTROL
# first using handtracking, then use hand landmarks to find the gesture of our hands, we will use the handtracking module.



# 1. importing cv2, time, and numpy after installing on pip
import cv2
import time
import numpy as np

# 13. import math to use hypotenuse function to determine length between index and thumb.
import math


# 8. Importing the HandTrackingModule, this is an absolute import, to execute this file we run computerVision/VolumeHandControlRoot.py
from HandTracking import HandTrackingModule as htm

#################################################
# 5. determining the height and width of the camera.
wCam, hCam = 640, 480
#################################################

# 2. check if webcam is working, VideoCapture(0) is normally laptop camera.
cap = cv2.VideoCapture(0)

# 6. using hCam and hCam here.
cap.set(3, wCam)
cap.set(4, hCam)

# 7. adding the framerate into the camera. 
pTime = 0

# 9. Creating the detector object, setting the detection confidence higher so the computer will be more 'certain' that it is detecting a hand.
detector = htm.handDetector(detectionCon=0.75)



# 15. installing pycaw, this package can change the volume of the laptop based on the length of the distance of index and thumb tips.  
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume.GetMute()
volume.GetMasterVolumeLevel()
volume.GetVolumeRange()
volume.SetMasterVolumeLevel(-20.0, None)


while True:
    # 3. checking the success of the camera capturing any image
    success, img = cap.read()

    # 9. looking for the location of the hands.
    img = detector.findHands(img)

    # 10. we need our landmark list to determine the positions of index and thumb. the full landmark list consist of 21 values.
    # 10. Before we print out the list of points, we have to make sure that there are points. Right below, we can get the list of landmarks and print the value of the particular point.

    # 10. we are getting landmarks 4(thumb) and 8(index)
    lmList = detector.findPosition(img, draw = False)
    if len(lmList) != 0:
        # print(lmList[4], lmList[8])
        
        # 11. making variables for circles for thumb and index tips.
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]

        # 12. getting the center of the line
        cx, cy  =  (x1 + x2) //2, (y1+y2) // 2

        # 11. making the landmarks on the tip of the thumb in index tip bigger
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        
        # 12. creating a line between the thumb and the index finger
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

        # 23. cirle for center of line between thumb and index
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        # 13. figuring out length of the thumb and index
        length = math.hypot(x2 - x1, y2-y1)
        print(length)

        # 14. determine the maximum and minimum length between thumb and index, and change the color of the circle when the length is below a certain value. 
        if length <20:
            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

    # 7. adding the framerate into the camera. 
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f"FPS: {int(fps)}", (40, 50), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    
    
    # 4. 
    cv2.imshow("Img", img)
    cv2.waitKey(1)
    