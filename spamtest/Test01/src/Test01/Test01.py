'''
Created on May 22, 2018

@author: Bo
'''
#import Tkinter
import cv2
print "hello world!"

img = cv2.imread("test02.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

img2 = img[000:600,200:400]


cv2.imshow("image",img)
cv2.imshow("image2",img2)
cv2.waitKey()