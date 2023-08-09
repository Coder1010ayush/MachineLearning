import cv2
import numpy as np


# img is a numpy array which stores an black image
img = np.zeros((400,400,3),np.uint8)

# img1 is a image of 3 Channel (red,blue,green)
img1 = cv2.imread("C:\\Users\\ayush\\Pictures\\Saved Pictures\\woman.jpg.jpg",1)
img1 = cv2.resize(img1,(500,500))

# showing image on the screen
print("image : ",img)
print("image 1 : ",img1)

# updating image
# 01 Sketching a line on the image
img = cv2.line(img,(0,0),(50,50),(255,255,255),4)
img1 = cv2.line(img1,(0,0),(100,100),(120,120,120),3)

# 02 Sketching circle on the image
img = cv2.circle(img,(100,100),50,(255,0,0),3)
img1 = cv2.circle(img1,(100,100),50,(255,0,0),3)

# 03 Sketching rectangle on the image
img = cv2.rectangle(img,(20,30),(90,120),(0,255,0),4)
img1 = cv2.rectangle(img1,(20,30),(90,120),(0,255,0),4)

# 04 Sketching ellipse on the image
img = cv2.ellipse(img,(170,180),(100,80),0,0,360,(0,255,255),5)
img1 = cv2.ellipse(img1,(160,170),(80,50),0,0,360,(0,0,255),5)

# how to put some text on the image
text = "Woman image"
text1 = "Black image"
font = cv2.FONT_HERSHEY_COMPLEX

img = cv2.putText(img,text1,(40,40),font,2,(255.255,255),2);
img1 = cv2.putText(img1,text,(40,40),font,2,(255,255,0),2);

cv2.namedWindow("Image Manipulation")
cv2.imshow("Image Manipulation",img)
cv2.imshow("Image",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()