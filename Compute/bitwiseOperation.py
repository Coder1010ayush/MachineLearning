import pyautogui as auto
import cv2
import sys
import numpy as np

img1 = np.full((500,500,3),200,dtype=np.uint8)
img2 = np.full((500,500,3),200,dtype=np.uint8)

cv2.circle(img1,(100,100),50,(255,255,255),-1)
cv2.circle(img2,(100,100),50,(0,0,0),-1)

andPic = cv2.bitwise_and(img2,img1)
cv2.imshow("andScreen",andPic)

orPic = cv2.bitwise_or(img2,img1)
cv2.imshow("ScreenOr",orPic)

xorPic = cv2.bitwise_xor(img2,img1)
cv2.imshow("xorScreen",xorPic)

notPic1 = cv2.bitwise_not(img1)
notPic2 = cv2.bitwise_not(img2)

cv2.imshow("notPicscreen1",notPic1)
cv2.imshow("notPicscreen2",notPic2)

cv2.imshow("screen1",img1)
cv2.imshow("screen2",img2)


key = cv2.waitKey(0)
if key == ord("q"):
    sys.exit()
cv2.destroyAllWindows()