from xml.etree.ElementTree import TreeBuilder
import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
pTime = 0

# import mediapipe functions and classes
# using mp faceDetection module:

mpFaceDetection = mp.solutions.face_detection
# importing the drawing module
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection()

while True:
    success, img = cap.read()

    # images are defaulted to BGR, we need to convert it into RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)
    # print(results)

    if results.detections:
        for id, detection in enumerate(results.detections):
            mpDraw.draw_detection(img, detection)
            # print(id, detection)
            # print(detection.score)
            print(detection.location_data.relative_bounding_box)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0 ), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1) 