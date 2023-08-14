import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys
import pyautogui

img = cv2.imread("Ballon.jpg")
img = cv2.resize(img,(500,500))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray,120,255,cv2.THRESH_BINARY)
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_limit = np.array([30,120,180])
upper_limit = np.array([40,255,255])

mask = cv2.inRange(hsv,lower_limit,upper_limit)
image = cv2.bitwise_and(img,img,mask= mask)
cv2.namedWindow("Screen")
# cv2.imshow("img",img)
# cv2.imshow("Screen",mask)
cv2.imshow("gray",gray)
# cv2.imshow("hsv",hsv)
cv2.imshow("image",image)
# cv2.imshow("thresh",thresh)
key = cv2.waitKey(0)
if key == ord("q"):
    sys.exit()
cv2.destroyAllWindows()