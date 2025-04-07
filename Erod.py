import cv2
import numpy as np

image = cv2.imread("ball.png",1)

kernel = np.ones((10,10),np.uint8)

image1 = cv2.erode(image,kernel)
cv2.imshow("Image",image)
cv2.imshow("Eroded Image",image1)

cv2.waitKey(0)

cv2.destroyAllWindows()
