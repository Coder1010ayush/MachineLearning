# -*- coding: utf-8 -*-
import cv2;
import pafy


video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
print(video)

# show video until camera is opened
# 0 shows the primary camera of laptop

while video.isOpened():
    ret,frame = video.read()
    if ret == True:
        frame = cv2.resize(frame,(500,500))
        cv2.imshow("frame", frame)
        key = cv2.waitKey(25)
        # if key == 0xff:
        #     break;
        print(key)
        
video.release()
cv2.destroyAllWindows()
