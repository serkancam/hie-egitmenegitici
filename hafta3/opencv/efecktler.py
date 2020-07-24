import numpy as np
import cv2


cap = cv2.VideoCapture(0)
while True:
    ret,frame =  cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    dusuk = np.array([30,150,50])
    yuksek = np.array([255,255,180])
    mask = cv2.inRange(hsv,dusuk,yuksek)
    sonuc = cv2.bitwise_and(frame,frame,mask=mask)
    blur = cv2.GaussianBlur(frame,(15,15),0)
    kernel = np.ones((15,15),np.float32)
    cv2.imshow("kemara1",sonuc)
    cv2.imshow("kamera2",blur)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cp.destroyAllWindows()
