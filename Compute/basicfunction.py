import sys
import cv2
import numpy as np
import pyautogui as auto

img = cv2.imread("C:\\Users\\ayush\\Pictures\\Saved Pictures\\woman.jpg.jpg", 1)
img = cv2.resize(img,(400,400))
cv2.imshow("Image",img)

pixel = img[120,300]
print("pixel : ",pixel)

# getting information about an image
print("size of image ",img.size) # number of pixels present in the image
print("dtype : ",img.dtype)
print("shape : ",img.shape)

redResolution = cv2.split(img)
greenResolution = cv2.split(img)
blueResolution = cv2.split(img)

print("red region : ",redResolution)
print("green region : ",greenResolution)
print("blue region : ",blueResolution)

red,blue,green = cv2.split(img)
cv2.imshow("red",red)
cv2.imshow("green",green)
cv2.imshow("blue",blue)

merg1 = cv2.merge((red,green,blue))
merg2 = cv2.merge((green,red,blue))
merg3 = cv2.merge((red,blue,green))
cv2.imshow("merge1",merg1)
cv2.imshow("merge2",merg2)
cv2.imshow("merge3",merg3)



key = cv2.waitKey(0)
if key == ord("q"):
    sys.exit()
cv2.destroyAllWindows()
