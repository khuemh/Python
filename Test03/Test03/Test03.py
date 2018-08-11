'''
Created on May 24, 2018

@author: Bo
'''
## Import Lib
import cv2
import numpy as np

'''Draw with cv2.line

## Add test.png to 'img'
img = cv2.imread("test.png")
## cv2.line(img, Startpoint, Endpoint, (B, G, R), LineWidth)
cv2.line(img, (0, 0), (614, 404), (0, 0, 200), 2)
cv2.line(img, (0, 404), (614, 0), (200, 0, 0), 2)
## Write to new.png
cv2.imwrite('new.png', img)
## Add new.png to 'new'
new = cv2.imread("new.png")
## Show 'new' in ImageBox
cv2.imshow("ImageBox", new)
'''

'''Draw with numpy'''

## Create new zeros img np.zeros((height, width, NumberOfColor))
img = np.zeros((600, 800, 3))

## Set img [:, :, (ColorChanel)]
img[300:600, 400:800, (0,2)] = 200 

## Draw line
#cv2.line(img, StartPoint, EndPoint, (200,100,0), 10)
for i in range(0, 600, 100):  
    cv2.line(img, (0,i), (800,i), (200,100,0), 5)
    cv2.putText(img, str(i), (4, i + 25), cv2.FONT_HERSHEY_TRIPLEX, 0.6, (200, 0, 0))
for i in range(0, 800, 200):
    cv2.line(img, (i, 0), (i, 600), (0, 0, 200), 5)  
    cv2.putText(img, str(i), (i + 4, 25), cv2.FONT_HERSHEY_COMPLEX, 0.6, (200, 0, 0))

## Draw Circle
#cv2.circle(img, CenterPoint, R, (B,G,R), Width)
cv2.circle(img, (400, 300), 100, (0, 200, 0), 3)

## Draw Ellipse
#cv2.ellipse(img, CenterPoint, (a_length, b_length), angle, StartAngle, EndAngle, Color)
cv2.ellipse(img, (400, 300), (200, 100), 0, 0, 360, (200, 2, 100), 3)
cv2.ellipse(img, (400, 300), (200, 100), 90, 0, 360, (200, 2, 100), 3)

## Draw Poly lines
#cv2.polylines(img, pts, isClolsed, color, Thickness, lineType, Shift)
pts1 = np.array(((200, 100), (600, 100), (400, 500)),np.int32)
pts1 = [pts1.reshape((-1, 1, 2))]
cv2.polylines(img, pts1, True, (200, 0, 0), 5)
pts2 = np.array(((200, 500), (600, 500), (400, 100)),np.int32)
pts2 = [pts2.reshape((-1, 1, 2))]
cv2.polylines(img, pts2, True, (0, 0, 200), 5)


cv2.imshow("ImageBox", img)

cv2.waitKey()
cv2.destroyAllWindows()

