'''
Created on May 30, 2018

@author: Bo
'''
import cv2
import numpy as np

## Set RGB var
r, g, b = 0, 0, 0
## Create RGB Function
def blue_funct(blue_val):
    global b
    b = blue_val
def green_funct(green_val):
    global g
    g = green_val
def red_funct(red_val):
    global r
    r = red_val
## Create trackbar
cv2.namedWindow("Image")
#cv2.createTrackbar(TrackbarName, windowName, val, count, onChange)
cv2.createTrackbar("BLUE", "Image", 0, 255, blue_funct)
cv2.createTrackbar("GREEN", "Image", 0, 255, green_funct)
cv2.createTrackbar("RED", "Image", 0, 255, red_funct)

while True:
    ## Create an empty image
    img = np.empty((600, 800, 3), np.uint8)
    ## Set RGB val to image
    img[:,:,0] = b 
    img[:,:,1] = g 
    img[:,:,2] = r
    cv2.imshow("Image", img)
    if cv2.waitKey(10) == ord('q'):
        break
    
cv2.destroyAllWindows()