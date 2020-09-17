import cv2

T = 200
lightCount = 0
im = cv2.imread("IMG_2490.JPG", cv2.IMREAD_GRAYSCALE)
#img_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#print(img_gray)
size = len(im) * len(im[0])
for i in range(len(im)):
    for j in range(len(im[i])):
        #print(im[i, j])
        if im[i, j] > T:
            lightCount += 1
            im[i, j] = 255

print("light = ", lightCount, "szie = ", size)
cv2.imshow('image',im)
cv2.waitKey(0)
cv2.destroyAllWindows()