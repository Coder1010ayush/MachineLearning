import cv2
import numpy as np
import pyautogui as auto

# auto.size() gives the size of the screen currently working on
screenResolution = auto.size()
path = "output.mp4"
fps = 20.0  # fps means frames per seconds
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter(path,fourcc,fps,screenResolution)

cv2.namedWindow("Live Recording ",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live Recording ",(600,600))

while True:
    img = auto.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output.write(frame)
    # cv2.imshow("res",frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
output.release()
cv2.destroyAllWindows()