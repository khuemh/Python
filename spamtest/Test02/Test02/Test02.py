'''
Created on May 23, 2018

@author: Bo
'''
import cv2
import numpy as np

img = np.empty((600,800,3))
cv2.imshow("Image", img)
cv2.waitKey()