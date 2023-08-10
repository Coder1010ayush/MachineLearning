import cv2
import numpy as np
import pyautogui as auto
import sys

img = np.array((400,400,3),np.uint16)*150
img = cv2.resize(img,(400,400))
cv2.rectangle(img,(200,300),(100,150),(255,0,255),3)

blank = np.array((400,400,3),np.uint16)*175
blank = cv2.resize(blank,(400,400))
cv2.rectangle(blank,(200,300),(100,150),(255,240,120),3)

output = img+blank
cv2.imshow("deform : ",output)

blended = cv2.add(img,blank)
cv2.imshow("blended",blended)

cv2.imshow("new Screen",blank)
cv2.imshow("Screen",img)

intersection = cv2.bitwise_and(img,blank)
cv2.imshow("intersection",intersection)

key = cv2.waitKey(0)
if key == ord("q"):
    sys.exit()
cv2.destroyAllWindows()