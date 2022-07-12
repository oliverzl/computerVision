FaceDetection Model provided by Google, running on CPU

________________________
FACEDETECTIONBASICS.PY
________________________



facedetection software that applies to videos, and/or cameras
this py file looks at the bare minimum code that is required to run facedetection

line 6: cap = cv2.VideoCapture("...") runs our video. (BEST TO USE WEBCAM, VIDEOS ABIT BUGGY)

line ?: success, img = cap.read(): gets our frame and puts it in variables success and img. 

pTime, cTime, fps, determines the video framerate, and cv2.putText shows the fps on the overlay of the video. cv2.putText has arguments that customize the look of the FPS

we can reduce framerate by increasing the argument value in cv2.waitKey(...)

Next Step: import mediapipe functions and classes so we can use them. 
we use mp.solutions.face_detection, and we get mp.solutions.drawing_utils to help us to draw without typing the drawing function ourselves. 

in total, we get 6 points for the face detection: 2 eyes, 2 points on the nose, and ears.

mpFaceDetection initialises the face detection module. 
by default, cv2 takes in images in BGR format, and now we convert it to RGB: imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

we use faceDetection to process the RGB and set it to the variable results: results = faceDetection.process(imgRGB)

print(results): the terminal will only pint results when it detects a face.
we need to extract the information out from results, so we can draw out the facedetection rectangle when any face is detected.

if results.detections is available: 
    for id, detection in results.detections
it will only print id, and detection if it detects a face. the score is in decimal, how much percentage the system thinks a face is displayed. within the location data is the bounding box. 0 label_id: 0 is face 0, 
1 label_id: 0 is the next face detected. label_id: 0 because both of them are faces. 

if we wanted the score, we would write results.detection.score
inside location data, we have relative bounding box. 

detection.location_data.relative_bounding_box.

xmin,ymin are all normalized values: values betwe   en 0 and 1.
we have to multiply xmin and ymin with the width and the height to get the pixel values, so that we can draw. 

We can also use the draw function itself to draw the landmarks

in the if results.detections: for id, detection in enumerate(results.detections), we can print the relative_bounding_box. 

when we run the file now, we see that the points on the face are not very useful,