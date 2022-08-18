import cv2
import mediapipe as mp      
import time

class FaceMeshDetector():
    def __init__(self, staticMode = False, maxFaces = 2, minDetectionCon = 0.2, minTrackCon=0.5):
        self.staticMode = staticMode
        self.maxFaces = maxFaces
        self.minDetectionCon = minDetectionCon
        self.minTrackCon = minTrackCon

        # using mediapipe to find the points on the face
        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(self.staticMode, self.maxFaces,self.minDetectionCon, self.minTrackCon)
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1)

    # class method findFaceMesh
    # we will have the option to draw or not draw
    def findFaceMesh(self, img, draw=True):
        # img is in bgr so we can convert it
        self.imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(self.imgRGB)
        # to display it:
        faces = []
        if self.results.multi_face_landmarks:
            # we may have multiple faces, so we must first loop through the faces, then we can draw.
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    # mpDraw.draw_landmarks is in mp.solutions
                    self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACE_CONNECTIONS, self.drawSpec, self.drawSpec)

                    # # finding out all the different points
                face = []
                for id,lm in enumerate(faceLms.landmark):
                    # print(lm)
                    #image height, width, channels 
                    ih, iw, ic = img.shape
                    x, y = int(lm.x*iw), int(lm.y*ih)
                    cv2.putText(img, str(id), (x,y), cv2.FONT_HERSHEY_PLAIN, 0.1, (0, 255, 0), 1)
                    # print(id, x, y) 
                    face.append([x,y])
            faces.append(face)
        return img, faces
    

def main():
    # getting the camera
    cap = cv2.VideoCapture(0)

# setting this to always run when the file runs
    pTime = 0
    detector = FaceMeshDetector()
    while True:
        success, img = cap.read()
        img, faces = detector.findFaceMesh(img)
        if len(faces)!= 0:
            print(faces[0])
        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime
        # the line below puts the fps value on the image
        cv2.putText(img, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 2555, 0), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()