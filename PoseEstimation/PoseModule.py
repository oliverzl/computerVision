# opencv: image processing
# mediapipe: pose estimation


# from unittest.loader import _SortComparisonMethod
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
# create a class with a method to detect the pose and method to find all the landmark points for us. 

class poseDetector():
    def __init__(self, mode=False, upBody=False, smooth=True, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        
        self.mpDraw = mp.solutions.drawing_utils 
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth,self.detectionCon, self.trackCon)

    # creating a class method to find the full pose
    def findPose(self, img, draw=True):
        # converting from BGR to RGB
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        # the draw is in the findPose method declaration on top
        # if landmarks are present, and then if draw is true: 
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img

    # detecting multiple specific points
    def findPosition(self, img, draw=True):
        lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                # print(id, lm)
                # to get pixel value:
                # pixel values of x and y of the landmark
                cx, cy = int(lm.x * w), int(lm.y*h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 3, (255, 0, 0), cv2.FILLED)
        return lmList
  

def main():
    # cv2.VideoCapture needs to have a relative path to the video
    cap = cv2.VideoCapture("PoseEstimation\PoseVideos\dancing.mp4")
    pTime = 0
    detector = poseDetector()
    # landmarks are in decimal places
    while True: 
        success, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.findPosition(img, draw=False)
        if len(lmList) != 0:
            print(lmList[14])
            cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv2.FILLED)
        # lmList = detector.findPosition(img)
        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        cv2.imshow('Image', img)
        # framerate
        cv2.waitKey(50)


if __name__ == "__main__":
    main()
