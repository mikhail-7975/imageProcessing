import cv2


im_gray = cv2.imread("sonetForLena.png", cv2.IMREAD_GRAYSCALE)
#(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst])
img_bw = cv2.adaptiveThreshold(im_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 19, 7);#cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]

cv2.imshow('image',img_bw)
cv2.waitKey(0)
cv2.destroyAllWindows()