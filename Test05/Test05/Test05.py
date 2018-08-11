'''
Created on May 30, 2018

@author: Bo
'''
import cv2
#import numpy as np

def get_val(pos):
    get_val.val = pos
get_val.val = 0
## Create Controll window
cv2.namedWindow("Controll window")
cv2.createTrackbar("Threshhold", "Controll window", 0, 255, get_val)

while True:
    # get image Test_im
    img = cv2.imread("Test_im1.png")
    cv2.imshow("Controll window", img)
    ## Thresh_hold
    # cv2.threshold(img, thresh, max_val, type)
    ret, img = cv2.threshold(img, get_val.val, 255, cv2.THRESH_TOZERO)
    if cv2.waitKey(10) == ord('q'):
        break
    # Show image
    cv2.imshow("Image", img)
cv2.destroyAllWindows()