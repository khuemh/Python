import cv2
import numpy as np

def h_min(pos):
    h_min.val = pos
h_min.val = 15
def s_min(pos):
    s_min.val = pos
s_min.val = 108
def v_min(pos):
    v_min.val = pos
v_min.val = 128
def h_max(pos):
    h_max.val = pos
h_max.val = 39
def s_max(pos):
    s_max.val = pos
s_max.val = 255
def v_max(pos):
    v_max.val = pos
v_max.val = 169

cv2.namedWindow("HSV_Tracking", cv2.WINDOW_FREERATIO)

cv2.createTrackbar("Min H", "HSV_Tracking", 0, 255, h_min)
cv2.createTrackbar("Max H", "HSV_Tracking", 255, 255, h_max)
cv2.createTrackbar("Min S", "HSV_Tracking", 0, 255, s_min)
cv2.createTrackbar("Max S", "HSV_Tracking", 255, 255, s_max)
cv2.createTrackbar("Min V", "HSV_Tracking", 0, 255, v_min)
cv2.createTrackbar("Max V", "HSV_Tracking", 255, 255, v_max)

arr_pnt = np.array((), np.int32)

cap = cv2.VideoCapture(0)
if (cap.isOpened() == False):
    print ("ERROR")
while (cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if ret == True:
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower = np.array([h_min.val, s_min.val, v_min.val])
        upper = np.array([h_max.val, v_max.val, v_max.val])
        mask_temp = cv2.inRange(hsv_frame, lower, upper)    
        kernel_er = np.ones((3,3))
        kernel_di = np.ones((5,5))
        mask_temp = cv2.erode(mask_temp, kernel_er)
        mask_temp = cv2.dilate(mask_temp, kernel_di, iterations = 3)
        #mask_temp = cv2.blur(mask_temp, (5,5), 0)
        cv2.putText(frame, "REC", (10, 20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,255), 1)
        cont = cv2.findContours(mask_temp, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]
        if len(cont) > 0:
            cont_tmp = cont[0]
            #cv2.drawContours(frame, cont, -1, (0, 255, 0), 2)
            M = cv2.moments(cont_tmp)
            x = int(M ['m10']/(M['m00']+1))
            y = int(M['m01']/(M['m00']+1))
            cv2.putText(frame, str((x,y)), (x-80, y-70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5, (255, 0, 0), 1)
            #epsilon = 0.1*cv2.arcLength(cont_tmp,True)
            #approx = cv2.approxPolyDP(cont_tmp,epsilon,True)
            #cv2.drawContours(frame, approx, -1, (0, 255, 0), 2)   
            #hull = cv2.convexHull(cont_tmp)
            #cv2.drawContours(frame, hull, -1, (0, 255, 0), 2)   
            rect = cv2.minAreaRect(cont_tmp)
            box = cv2.boxPoints(rect)
            box = np.intc(box)
            cv2.drawContours(frame,[box],0,(0,255,0),2)
            arr_pnt = np.append(arr_pnt, (int(x), int(y)))
            if len(arr_pnt) > 200:
                arr_pnt = np.delete(arr_pnt, (0, 1))
            arr_pnt = np.reshape(arr_pnt, (-1, 1, 2))
            cv2.polylines(frame, [arr_pnt], False, (0, 255, 0), 2)
            
            
        mask = cv2.merge((mask_temp, mask_temp, mask_temp))
        result = cv2.bitwise_and(frame, mask)
        #cv2.imshow("HSV_Tracking", mask)
        cv2.imshow("Frame", frame)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()