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

mpDraw = mp.solutions.drawing_utils 
mpPose = mp.solutions.pose
pose = mpPose.Pose()

# cv2.VideoCapture needs to have a relative path to the video
cap = cv2.VideoCapture("PoseEstimation\PoseVideos\jogging.mp4")
pTime = 0

# landmarks are in decimel places

while True: 
    success, img = cap.read()
    # converting from BGR to RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    # print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            # print(id, lm)
            # to get pixel value:
            # pixel values of x and y of the landmark
            cx, cy = int(lm.x * w), int(lm.y*h)
            cv2.circle(img, (cx, cy), 3, (255, 0, 0), cv2.FILLED)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow('Image', img)
    # framerate
    cv2.waitKey(20)
