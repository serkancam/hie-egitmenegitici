import cv2
import numpy as np
img =  cv2.imread(r"hafta3/opencv/resim.jpg")
cv2.imshow("ilk",img)

# print(img)
cv2.waitKey(0)
cv2.destroyAllWindows()