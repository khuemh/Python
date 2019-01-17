import cv2
import numpy as np
from cv2 import getDerivKernels
## Blue value define Function
# Min value
def b_min(pos):
    b_min.val = pos
b_min.val = 65    
def g_min(pos):
    g_min.val = pos
g_min.val = 15  
def r_min(pos):
    r_min.val = pos
r_min.val = 167  
# Max value
def b_max(pos):
    b_max.val = pos
b_max.val = 192 
def g_max(pos):
    g_max.val = pos
g_max.val = 122 
def r_max(pos):
    r_max.val = pos
r_max.val = 255 
## Create Trackbar
cv2.namedWindow("Tracking")
## RGB value trackbar
# Blue value
cv2.createTrackbar("Min BLUE", "Tracking", 0, 255, b_min) 
cv2.createTrackbar("Max BLUE", "Tracking", 255, 255, b_max)
# Green value
cv2.createTrackbar("Min GREEN", "Tracking", 0, 255, g_min)
cv2.createTrackbar("Max GREEN", "Tracking", 255, 255, g_max)
# Red value 
cv2.createTrackbar("Min RED", "Tracking", 0, 255, r_min)
cv2.createTrackbar("Max RED", "Tracking", 255, 255, r_max)


# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture(0) 
# Check if camera opened successfully
if (cap.isOpened()== False): 
    print("Error opening video stream or file")
# Read until video is completed
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    
    if ret == True:     
        # Display the resulting frame
        cv2.imshow('Tracking',frame)   
        ## Tracking
        lower = np.array([b_min.val, g_min.val, r_min.val])
        upper = np.array([b_max.val, g_max.val, r_max.val])
        #cv2.inRange(src, lower, upper)
        mask_tmp = cv2.inRange(frame, lower, upper)
        # Create Kernel Filter
        '''kernel = np.array([[1, 1, 1, 1],
                           [1, 1, 1, 1],
                           [1, 1, 1, 1],
                           [1, 1, 1, 1]])'''
        kernel_er = np.ones((3,3))
        kernel_di = np.ones((5,5))
        # Erode
        mask_tmp = cv2.erode(mask_tmp, kernel_er)
        # Dilate
        mask_tmp = cv2.dilate(mask_tmp, kernel_di)
        # Merge
        mask = cv2.merge((mask_tmp, mask_tmp, mask_tmp))
        # result = "frame" AND "mask"
        result = cv2.bitwise_and(frame, mask)
        # Show Result
        cv2.imshow('Mask Frame', mask)
        cv2.imshow('Result', result)
        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break    
    # Break the loop
    else: 
        break 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()