import cv2
import numpy as np

cam = cv2.VideoCapture(0) # link to webcam
face_cascade = cv2.CascadeClassifier() # create classifier
eyes_cascade = cv2.CascadeClassifier() # create classifier
face_cascade.load(r'classifier\haarcascade_frontalface_default.xml') # load classifier
eyes_cascade.load(r'classifier\haarcascade_eye.xml') # load classifier
while cam.isOpened():
    status, img = cam.read()
    if status is None:
        break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert to grayscale (2D)
    gray = cv2.equalizeHist(gray) # equalize histogram - improve contrast
    faces = face_cascade.detectMultiScale(gray) # detect faces
    height, width, _ = img.shape
    if len(faces) > 0:
        cv2.putText(
            img, f'Faces detected: {len(faces)}', (10, height-30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2
        )
        for i, (x, y, w, h) in enumerate(faces):
            # draw rectangle around face
            cv2.rectangle(
                img, (x, y), (x+w, y+h), (0, 255, 0), 1
            )
            # display person number
            cv2.putText(
                img, f'Person {i+1}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2
            )
            # faceROI
            faceROI = gray[y:y+h, x:x+w]
            eyes = eyes_cascade.detectMultiScale(faceROI)
            if len(eyes) > 0:
                for (ex, ey, ew, eh) in eyes:
                    center = (x + ex + ew//2, y + ey + eh//2)
                    radius = int(round((ew + eh)*0.25))
                    cv2.circle(
                        img, center, radius, (255, 0, 0), 1
                    )
            
    else:
        # display no face found
        cv2.putText(
            img, 'No face found', (10, height-30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2
        )
    
    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
cam.release()