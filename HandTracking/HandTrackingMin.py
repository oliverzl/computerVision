import cv2
import mediapipe as mp
import time

# using the laptop's webcam
cap = cv2.VideoCapture(0)

print(type(cv2.VideoCapture))


# create an object from class Hands
# related to hand detection module

# mpHands.Hands:
# static_image_mode: False, so that class can detect keep tracking with a good tracking confidence. if tracking confidence drops below a certain range, it will stop tracking and perform detection. 
# max_hands, min tracking confidence and min detection confidence


mpHands = mp.solutions.hands
# default parameters in .Hands()
hands = mpHands.Hands(static_image_mode=False,
               max_num_hands=4,
               min_detection_confidence=0.5,
               min_tracking_confidence=0.5)

# to draw the connections between landmarks in hands
mpDraw = mp.solutions.drawing_utils

# checking framerate
pTime = 0
cTime = 0




# running the webcam itself, infinite loop while True
while True:
    # this gives us our frame
    success, img = cap.read()

    # in this while True loop, send in our RGB image to this object.
    # imgRBG is the conversion from normal image to RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # taking the converted image, process the frames for us, gives us the results
    results = hands.process(imgRGB)

    # checking if hand is detected or not
    # put in a FOR loop to check for multiple hands


        # results.multi_hands_landmarks means the results var detected hands:
    if results.multi_hand_landmarks:
        # handLms is a single hand
        # for every hand inside results.multi_hand_landmarks
        for handLms in results.multi_hand_landmarks:
            # get info in hand: ID number and landmark info
            # landmark info gives x and y coordinate
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                # get height, width and channel from img
                h, w, c = img.shape
                # landmark.x * width, landmark.y * height
                cx, cy = int(lm.x*w), int(lm.y*h)
                
                if id == 0:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    # putting text inside to show FPS

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 2)


    cv2.imshow("Image", img)
    cv2.waitKey(1)
