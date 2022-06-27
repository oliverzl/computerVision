import cv2
import mediapipe as mp
import time

# create an object from class Hands
# related to hand detection module

# mpHands.Hands:
# static_image_mode: False, so that class can detect keep tracking with a good tracking confidence. if tracking confidence drops below a certain range, it will stop tracking and perform detection. 
# max_hands, min tracking confidence and min detection confidence


# basic parameters in the class for the hands
class handDetector():
    def __init__(self, mode=False, maxHands=4, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        # default parameters in .Hands()    
        # hands = mpHands.Hands()
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
        # to draw the connections between landmarks in hands
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True): 
    # in this while True loop, send in our RGB image to this object.
    # imgRBG is the conversion from normal image to RGB
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # taking the converted image, process the frames for us, gives us the results
        self.results = self.hands.process(imgRGB)

    # checking if hand is detected or not
    # put in a FOR loop to check for multiple hands
        # results.multi_hands_landmarks means the results var detected hands:
        if self.results.multi_hand_landmarks:
            # handLms is a single hand
            # for every hand inside results.multi_hand_landmarks
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img
    


    def findPosition(self, img, handNo=0, draw=True):

        lmList = []
        # check if any hands were detected or not.
        # it will get the first hand, and within the hand, it gets all the landmarks and puts them in a list
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            # get info in hand: ID number and landmark info
            # landmark info gives x and y coordinate
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                # get height, width and channel from img
                h, w, c = img.shape
                # landmark.x * width, landmark.y * height
                cx, cy = int(lm.x*w), int(lm.y*h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                if id == 0:
                    # if draw:
                        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        return lmList

def main():
    pTime = 0
    cTime = 0
    # using our webcam
    cap = cv2.VideoCapture(0)
    detector = handDetector()

# running the webcam itself, infinite loop while True
    while True:
        # this gives us our frame
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        # if len(lmList) != 0:
        #     print(lmList[4])
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        # putting text inside to show FPS
        # cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 2)
        cv2.imshow("Image", img)
        cv2.waitKey(1)




#if we are running this script, do this
# whatever we write in the main() part, will be a dummy code that is used to showcase the features of the module

if __name__ == "__main__":
    main()
