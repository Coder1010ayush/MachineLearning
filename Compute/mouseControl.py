import cv2
import numpy as np
import pyautogui as auto

def draw(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(100,100),35,(0,255,255),4)
    elif event == cv2.EVENT_LBUTTONUP:
        cv2.ellipse(img,(200,200),(100,80),0,0,360,(0,255,255),4)
    else:
        cv2.rectangle(img,(100,120),(150,160),(255,255,0),3)
    print(flags)
    print(param)

cv2.namedWindow("Mouse Event Listener")
img = np.zeros((400,400,3),np.uint8)
# function which takes instruction from mouse
cv2.setMouseCallback("Mouse Event Listener", draw)
while True:
    cv2.imshow("Mouse Event Listener",img)
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()