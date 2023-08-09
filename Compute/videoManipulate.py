import cv2
import numpy as np
import pafy
import datetime

video = cv2.VideoCapture(0)
print(video)

while video.isOpened():
    ret,frame = video.read()
    if ret:
        cv2.resize(frame,(600,600))
        font = cv2.FONT_HERSHEY_COMPLEX
        text = "live"
        frame = cv2.putText(frame,text,(20,50),font,1,(0,255,255),1,cv2.LINE_AA)
        frame = cv2.rectangle(frame,(60,70),(100,110),(0,0,255),-1)
        frame = cv2.ellipse(frame,(180,200),(100,80),0,0,360,(0,255,255),2)
        cv2.imshow("video",frame)

        key = cv2.waitKey(25)
        if key == ord("q"):
            break
video.release()
cv2.destroyAllWindows()