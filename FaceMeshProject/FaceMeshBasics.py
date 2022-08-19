import cv2
import mediapipe as mp      
import time


# getting the camera
cap = cv2.VideoCapture(0)

# setting this to always run when the file runs
pTime = 0


# using mediapipe to find the points on the face
mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1)

while True:
    success, img = cap.read()
    # img is in bgr so we can convert it
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    # to display it:
    if results.multi_face_landmarks:
        # we may have multiple faces, so we must first loop through the faces, then we can draw.
        for faceLms in results.multi_face_landmarks:
            # mpDraw.draw_landmarks is in mp.solutions
            mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACE_CONNECTIONS, drawSpec, drawSpec)
            # finding out all the different points
            for id,lm in enumerate(faceLms.landmark):
                # print(lm)
                #image height, width, channels
                ih, iw, ic = img.shape
                x, y = int(lm.x*iw), int(lm.y*ih)
                print(id, x, y)
                
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    # the line below puts the fps value on the image
    cv2.putText(img, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 2555, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)


