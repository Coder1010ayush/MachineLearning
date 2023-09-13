import cv2
import numpy as np
import datetime

video = cv2.VideoCapture(0)
print(video)

while video.isOpened():
    ret,frame = video.read()
    if ret:
        cv2.resize(frame,(1280,720))
        font = cv2.FONT_HERSHEY_COMPLEX
        text = "live"
        frame = cv2.putText(frame,text,(20,50),font,1,(0,255,255),1,cv2.LINE_AA)
        
        cv2.imshow("video",frame)

        key = cv2.waitKey(25)
        if key == ord("q"):
            break
video.release()
cv2.destroyAllWindows()
# import sys
# def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

# Arr = get_ints()
# print(Arr)