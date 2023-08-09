import cv2;

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
output = cv2.VideoWriter("output.mp4",fourcc,20.0,(600,600)) # fileName , fourcc or video ,fps(freame per second),frame resolution
video = cv2.VideoCapture(0,cv2.CAP_DSHOW) 
print(video)

# show video until camera is opened
# 0 shows the primary camera of laptop
while video.isOpened():
    ret,frame = video.read()
    if ret:
        frame = cv2.resize(frame,(500,500))
        cv2.imshow("frame", frame)
        output.write(frame)
        key = cv2.waitKey(25)
        # if key == 0xff:
        #     break;
        # print(key)
output.release()        
video.release()
cv2.destroyAllWindows()
