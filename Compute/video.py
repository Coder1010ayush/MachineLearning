# -*- coding: utf-8 -*-
import cv2

# Capturing video through primary camera of laptop
video = cv2.VideoCapture("/PATH")
print(video)
while True:
    ret,frame = video.read();  
    frame =cv2.resize(frame,(500,500))
    grayScale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame",frame)
    k = cv2.waitKey(30)
    if k == ord("q"):
        break;

#release all resources when program is terminated
cv2.release()
cv2.destroyAllWindows()
    
