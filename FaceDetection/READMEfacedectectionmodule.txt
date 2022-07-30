we will now create a module out of the face detection basics so that we do not repeat unnecessary code. 

the first thing we need for our module is the if statement:
if __name__ == "__main__".

now, we need to put everything related to initialisations into the class FaceDetector()

we switch everything to class instance variables. 
now, the findFaces class method needs to return something. 
we can return the bounding box information, the id, and the score:
create a new list = bboxs (bounding boxes)
currently, all of the code in self.results.detections is only for a single face. 
whenever it processes, we need to put it in our bounding boxes list. 

now, in the main(), we have to create an object from our FaceDetector class, detector. 


we can print out the bboxs list, which gives us information: 
it shows a list of lists (if there are multiple faces: the face number id: 1 face is index 0, the position of the bounding box, and the confidence. )

adding additional things now: making the corners of the bounding box thicker to emphasise on the targeting of the face: fancyDraw.
parameters include l=length, and size=thickness=t

first, we extract x, y, w, and h from the bounding box. 
x1 and y1 are corner points
cv2.line(img, (x, y) , (x+l, y), (255, 0, 255), t) draws a line at the top left hand corner.
 we set and comment out for the top left target piece:
now, all four corners are completed.

now, in the main() function, if  img, bboxs = detector.findFaces(img, False) instead of img, bboxs = detector.findFaces(img), 
it will not draw. 
the box drawing function is in findFaces, if draw: img = self.fancyDraw(img, bbox)