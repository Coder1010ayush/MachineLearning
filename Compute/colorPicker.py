import cv2
import numpy as np

img = np.zeros((300,300,3),np.uint8)
cv2.namedWindow("Color Picker")
def test(x):
    pass
setTrackBar = "0:OFF\n1:ON"
cv2.createTrackbar(setTrackBar,"Color Picker",0,1,test)

rTrackBar = "Red : "
cv2.createTrackbar(rTrackBar,"Color Picker",0,255,test)

gTrackBar = "Green : "
cv2.createTrackbar(gTrackBar,"Color Picker",0,255,test)

bTrackBar = "Blue : "
cv2.createTrackbar(bTrackBar,"Color Picker",0,255,test)

while True:
    cv2.imshow("Color Picker",img)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

    setBar = cv2.getTrackbarPos(setTrackBar,"Color Picker")
    red = cv2.getTrackbarPos(rTrackBar, "Color Picker")
    green = cv2.getTrackbarPos(gTrackBar, "Color Picker")
    blue = cv2.getTrackbarPos(bTrackBar, "Color Picker")

    if setBar==0:
        img[:] =0
    else:
        img[:] = [red,green,blue]


cv2.destroyAllWindows()
