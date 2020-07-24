import cv2
import numpy as np
img =  cv2.imread(r"hafta3/opencv/resim.jpg")

cv2.line(img,(0,0),(150,200),(255,255,255),10)
cv2.rectangle(img,(15,25),(200,150),(255,0,255),-1)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"10 dk ara", (0,130),font,1,(255,0,0),2,cv2.LINE_AA)

cv2.imshow("ilk",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
