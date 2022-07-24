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

