# opencv: image processing
# mediapipe: pose estimation

import cv2
import mediapipe as mp
import time

# mp.solutions.pose init():
    # def __init__(self,
    #             static_image_mode=False,
    #             upper_body_only=False,
    #             smooth_landmarks=True,
    #             min_detection_confidence=0.5,
    #             min_tracking_confidence=0.5):

# detection needs higher than 0.5 to enable tracking. 

mpPose = mp.solutions.pose
pose = mpPose.Pose()

# cv2.VideoCapture needs to have a relative path to the video
cap = cv2.VideoCapture("PoseEstimation\PoseVideos\walking.mp4")
pTime = 0

while True: 
    success, img = cap.read()
    

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow('Image', img)
    # framerate
    cv2.waitKey(1)
