import cv2
import numpy as np
img =  cv2.imread(r"hafta3/opencv/resim.jpg")
gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# retval,treshold = cv2.threshold(img,10,255,cv2.THRESH_BINARY)
retval,treshold = cv2.adaptiveThreshold(gri,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

cv2.imshow("ilk",img)
cv2.imshow("esik",treshold)

cv2.waitKey(0)

cv2.destroyAllWindows()