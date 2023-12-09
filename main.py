import cv2
import numpy as np
import imutils

cap=cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)

while True:
    rat,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    mask=cv2.inRange(hsv,lower_yellow,upper_yellow)
    cnts=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnts=imutils.grab_contours(cnts)

    for c in cnts:
        area=cv2.contourArea(c)
        cv2.drawContours(frame,[c],-1,(0,255,0),3)

        M=cv2.moments(c)
        if M["m00"]!=0:
            cx=int(M["m10"]/M["m00"])
            cy=int(M["m01"]/M["m00"])
            cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
            cv2.putText(frame,"Center",(cx-20,cy-200),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
            cv2.imshow("frame",frame)
            cv2.waitKey(10)


    print("area is.....", area)
    print("centroid is at", cx, cy)

    k=cv2.waitKey(200)
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()