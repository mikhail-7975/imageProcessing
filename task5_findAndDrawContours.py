import cv2

T = 200
lightCount = 0
#im = cv2.imread("Flag_of_Japan.svg.png")
im = cv2.imread("middle.png")
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)#cv2.imread("mountain.jpg", cv2.IMREAD_GRAYSCALE)

ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(im, contours, -1, (0,255,0), 1)

cv2.imshow('image', im)
cv2.waitKey(0)
cv2.destroyAllWindows()