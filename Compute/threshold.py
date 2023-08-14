import sys
import cv2
import numpy as np
import  pyautogui as  auto
import matplotlib.pyplot as plt

img = cv2.imread("chhota bheem.jpg")
img = cv2.resize(img,(600,600))
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray_img,100,255,cv2.THRESH_BINARY)
kernal = np.ones((3,3),np.uint8)
erode_img = cv2.erode(gray_img,kernal)

# cv2.imshow("Chhota Bheem",img)
# cv2.imshow("Gray Image",gray_img)
# cv2.imshow("Thresh",thresh)
# cv2.imshow("erode",erode_img)

list = [img,gray_img,erode_img,thresh]
title = ["Chhota Bheem","Grey Image","erode","thresh"]
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(list[i],'gray')
    plt.title(title[i])
    plt.xticks([])
    plt.yticks([])
plt.show()

key = cv2.waitKey(0)
if key == ord("q"):
    sys.exit()
cv2.destroyAllWindows()