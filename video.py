import cv2
import numpy as np

cam = cv2.VideoCapture(r'C:\Users\ZAID\Videos\warhaven quadra kill.mp4') # link to webcam

while cam.isOpened():
    status, img = cam.read()
    if status is None:
        break
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    stack = np.hstack((img, rgb))
    resized = cv2.resize(stack, None, fx=0.5, fy=0.5)
    cv2.imshow('Webcam', resized)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
cam.release()