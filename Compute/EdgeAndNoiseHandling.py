import numpy  as np
import cv2
import pyautogui as auto
import matplotlib.pyplot as plt
import sys

img = cv2.imread("chhota.jpg")
img = cv2.resize(img,(500,500))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,140,255,cv2.THRESH_BINARY_INV)
kernal = np.zeros((5,5),np.uint8)
erode = cv2.erode(thresh,kernal)
dia = cv2.dilate(thresh,kernal)
cv2.imshow("img",img)
cv2.imshow("gray",gray)
cv2.imshow("thresh",thresh)
cv2.imshow("erode",erode)
cv2.imshow("dialation",dia)
key = cv2.waitKey(0)
if key == ord("q"):
    sys.exit()
cv2.destroyAllWindows()

