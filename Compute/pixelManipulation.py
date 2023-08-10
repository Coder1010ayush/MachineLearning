import numpy
import numpy as np
import cv2
import pyautogui as auto
import sys

img = cv2.imread("C:\\Users\\ayush\\Pictures\\Saved Pictures\\woman.jpg.jpg", 1)
img = cv2.resize(img,(500,500))

cv2.namedWindow("Screen")
img = cv2.copyMakeBorder(img,3,3,3,3,cv2.BORDER_CONSTANT,(255,255,0))
cv2.imshow("Screen",img)

blank = numpy.ones((400,400,3),np.uint8)*255
cv2.rectangle(blank,(50,150),(100,200),(0,0,255),3,1)
blank = cv2.copyMakeBorder(blank,3,3,3,3,cv2.BORDER_CONSTANT,(255,255,0))
cv2.imshow("Blank ",blank)

key = cv2.waitKey(0)
if key == ord("q"):
    sys.exit()
cv2.destroyAllWindows()