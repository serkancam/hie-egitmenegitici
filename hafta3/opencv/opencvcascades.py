
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(r"hafta3/opencv/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(r"hafta3/opencv/haarcascade_eye.xml")
while True:
    ret,frame = cap.read()
    gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    yuzler = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in yuzler:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray,1.2)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
            # blur = cv2.GaussianBlur(roi_color,(10,10),0)

    cv2.imshow('kamera1',frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()