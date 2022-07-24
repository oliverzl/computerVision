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

xmin,ymin are all normalized values: values between 0 and 1.
we have to multiply xmin and ymin with the width and the height to get the pixel values, so that we can draw. 

We can also use the draw function itself to draw the landmarks

in the if results.detections: for id, detection in enumerate(results.detections), we can print the relative_bounding_box. 

when we run the file now, we see that the points on the face are not very useful.
detection.location_data.relative_bounding_box.xmin is a very long call, so we need to shorten it. 
we will store the information in a bounding box, then we will extract it.

bboxC = detection.location_data.relative_bounding_box.xmin.
we will then convert it so we can work with pixel values.

we will take the return values of img.shape, imageheight (ih), imagewidth(iw), and imagechannels(ic).

bbox is set to have xmin, ymin, width and height: 
int(bboxC.xmin * iw), int(bboxC.ymin * ih) \ 
int(bboxC.xmin * iw), int(bboxC.ymin * ih).


now, we can cv2.rectangle, putting in the image and the boundingbox which contains all 4 values, and we make the box colour purple.

now, we are not using the default function (mpDraw.draw_detection(img, detection)) to draw. We are taking in the variables detected by the module and using those values to draw. 

to change the minimum =face detection confidence (sensitivity), change mpFaceDetection.FaceDetection to a higher number, 0.75.

we can also set to see the confidence value: we can put it on the bounding box.

setting it to percentages with putText. now, we can see the detection confidence. the bounding box disappears totally when the confidence drops below 75%, as set in faceDetection = mpFaceDetection.FaceDetection(0.75).

box[1] - 20 makes the percentage info abit higher than the actual bounding box, so we can see it clearly, and setting it to purple. the last argument, 2, sets the size. 