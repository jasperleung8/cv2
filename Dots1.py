import cv2
import numpy as np

dot1 = cv2.imread("input1.png")
dot2 = cv2.imread("input2.png")

img1 = cv2.addWeighted(dot1,0.5,dot2,0.4,1.5)
img2 = cv2.addWeighted(dot1,0.5,dot2,0.4,0)

cv2.imshow("Bright",img1)
cv2.imshow("Bright",img2)

cv2.waitKey(0)

cv2.destroyAllWindows()
