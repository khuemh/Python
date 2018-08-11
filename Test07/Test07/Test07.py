import cv2
import numpy as np
import time
## Declare
def Mouse_event(event, x, y, f, frame):
    if event == cv2.EVENT_LBUTTONDOWN:
        Mouse_event.x0 = x 
        Mouse_event.y0 = y 
        Mouse_event.draw = True
    if event == cv2.EVENT_LBUTTONUP:
        Mouse_event.x1 = x 
        Mouse_event.y1 = y 
        Mouse_event.draw = False
        min_y = min([Mouse_event.y0, Mouse_event.y1])
        min_x = min([Mouse_event.x0, Mouse_event.x1])
        max_y = max([Mouse_event.y0, Mouse_event.y1])
        max_x = max([Mouse_event.x0, Mouse_event.x1])
        Mouse_event.frame = frame[min_y : max_y, min_x : max_x]
    if event == cv2.EVENT_MOUSEMOVE:
        Mouse_event.x = x 
        Mouse_event.y = y 
Mouse_event.frame = None
Mouse_event.x0 = 0 
Mouse_event.y0 = 0 
Mouse_event.x1 = 0
Mouse_event.y1 = 0
Mouse_event.x = 0
Mouse_event.y = 0
Mouse_event.draw = False

cap = cv2.VideoCapture(0)
if (cap.isOpened() == False):
    print("ERROR!")
while(cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_tmp = frame.copy()
    if ret == True:
        ## BEGIN
        #frame_tmp = cv2.cvtColor(frame_cop, cv2.COLOR_BGR2GRAY)
        if Mouse_event.draw:
            frame_tmp = cv2.rectangle(frame_tmp, (Mouse_event.x0, Mouse_event.y0), (Mouse_event.x, Mouse_event.y), (0, 255, 0), 1)
        if Mouse_event.frame is not None:
            match = cv2.matchTemplate(frame_tmp, Mouse_event.frame, cv2.TM_CCORR_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match)
            if max_val > 0.9:                
                cv2.putText(frame_tmp, "%.2f" %max_val, max_loc, cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,0,0), 2)
                h, w, d = Mouse_event.frame.shape
                cv2.rectangle(frame_tmp, max_loc, (max_loc[0]+w, max_loc[1]+h), (0,255,0), 2)
            #cv2.circle(frame_tmp, max_loc, 5, (0,0,255), -1)
            cv2.imshow("Match", match)
            cv2.imshow("Sample", Mouse_event.frame)            
        cv2.imshow("Tracking", frame_tmp)
        cv2.setMouseCallback("Tracking", Mouse_event, frame)    
        ## END
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    else:
        break
cap.release() 
cv2.destroyAllWindows()