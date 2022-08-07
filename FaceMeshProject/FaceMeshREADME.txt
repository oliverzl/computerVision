FaceMesh Detection:
learn how to detect 468 landmarks on faces.
runs in cpu and mobile devices.\

we will first create a basics file, so we can make a module from it to use freely.

in mp.solutions.face_mesh: we can see the FaceMesh class:
ctrl click mp.solutions, .facemesh
static_image_mode = False: static_image_mode is to see if we are using it only for detection, or detection and tracking.

if static_image_mode is True, it will detect in every image. However, if it is false, it will detect and track. 


draw_landmarks: 
we can see that we have the image, landmark_list, and the connections arguments:

if results.multi_face_landmarks is the drawing function. 