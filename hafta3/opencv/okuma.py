
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
img = cv2.imread()
gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
w,h = gri.shape[::-1]
while True:
    ret,frame = cap.read()
    griFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    sonuc = cv2.matchTemplate(griFrame,gri,cv2.TM_CCOEFF_NORMED)
    thresh = 0.5
    loc = np.where(sonuc>=thresh)
    
    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame,pt,(pt[0]+w,pt[1]+h),(255,255,255),2)


    cv2.imshow('kamera1',frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()