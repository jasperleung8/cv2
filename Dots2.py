import cv2

dot1 = cv2.imread("input1.png")
dot2 = cv2.imread("input2.png")

img = cv2.addWeighted(dot1,0.5,dot2,0.4,1.5)
sub = cv2.subtract(img,dot2)

cv2.imshow("3 dot",img)
cv2.imshow("2 dot",dot2)
cv2.imshow("subtracted",sub)

cv2.waitKey(0)

cv2.destroyAllWindows()
