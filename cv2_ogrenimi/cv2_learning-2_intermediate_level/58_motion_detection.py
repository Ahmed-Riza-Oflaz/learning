import cv2
import numpy as np

af = cv2.FONT_HERSHEY_COMPLEX
bf = cv2.FONT_HERSHEY_COMPLEX_SMALL
cf = cv2.FONT_HERSHEY_DUPLEX
df = cv2.FONT_HERSHEY_PLAIN
ef = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
ff = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
gf = cv2.FONT_HERSHEY_SIMPLEX
kf = cv2.FONT_HERSHEY_TRIPLEX
jf = cv2.FONT_ITALIC

#------FONTS--------

cap = cv2.VideoCapture("kosan_insan-1.mp4")

ret , frame1 = cap.read()
ret ,frame2 = cap.read()

while cap.isOpened():

    frame1 = cv2.resize(frame1,(640,480))
    frame2 = cv2.resize(frame2,(640,480))

    diff = cv2.absdiff(frame1,frame2)

    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray,(5,5),0)

    _,thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)

    dilated = cv2.dilate(thresh,None,iterations= 2)

    contours,_ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(frame1,contours,-1,(0,0,255),4)

    cv2.imshow("frame",frame1)

    frame1 = frame2

    ret,frame2 = cap.read()


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()