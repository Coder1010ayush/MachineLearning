import sys
import cv2
import numpy as np
import pyautogui as auto

img = cv2.imread("C:\\Users\\ayush\\Pictures\\Saved Pictures\\woman.jpg.jpg", 1)
img = cv2.resize(img,(500,500))
cv2.imshow("screen",img)
regionOfInterest = img[0:400,0:500]
cv2.imshow("new Screen",regionOfInterest)

key = cv2.waitKey(0)
if key == ord("q"):
    sys.exit()

cv2.destroyAllWindows()