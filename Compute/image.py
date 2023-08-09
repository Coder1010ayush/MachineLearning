# -*- coding: utf-8 -*-
import cv2

# 1 means it has image will have rgb color
img1 = cv2.imread("C:\\Users\\ayush\\Pictures\\Saved Pictures\\woman.jpg.jpg", 1)
img2 = cv2.imread("C:\\Users\\ayush\\Pictures\\Saved Pictures\\woman.jpg.jpg", 0)

# image in computer stores as multidimensional matrix or array(numpy array in python)
# print(img1)
img1 = cv2.resize(img1, (400, 400))
img2 = cv2.resize(img2, (400, 400))
img1 = cv2.flip(img1, 1);
img2 = cv2.flip(img2, -1)

cv2.imshow("original", img1)
cv2.imshow("Gray Scale picture ", img2)

'''
img2 = cv2.resize(img2,(400,400))
cv2.imshow("original",img2)
cv2.imshow("Gray Scale picture ",img2) '''

# saving image after some operation performed on it
cv2.imwrite("C:\\Users\\ayush\\Pictures\\Saved Pictures\\grayImage.jpg", img2)

# waitKey help us to hold image or video on the screen
# 0 - static otherwise time will be in milliseconds
key = cv2.waitKey(0)
print(key)

# destroyAllWindows() help us to release or free up the acquired space by the program in the memory
cv2.destroyAllWindows()
