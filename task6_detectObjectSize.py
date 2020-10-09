import cv2

#image = cv2.imread("big.png")
#image = cv2.imread("middle.png")
#image = cv2.imread("small.png")
image = cv2.imread("bumerang.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

heigh = len(gray)
width = len(gray[0])

# Find bounding box
x,y,w,h = cv2.boundingRect(thresh)
cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
cv2.putText(image, "w={},h={}".format(w,h), (x,y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (36,255,12), 2)

objWidth = w
objHeigh = h

print("S = ", heigh * width)
print("obj S = ", objHeigh * objWidth)

partOfImage = (objHeigh * objWidth / (heigh * width))

if(partOfImage > 0.3):
    print("this object is big")
elif(partOfImage > 0.15):
    print("this object is middle")
else:
    print("this object is small")

#cv2.imshow("thresh", thresh)
cv2.imshow("image", image)
cv2.waitKey()

'''
im = cv2.imread("Flag_of_Japan.svg.png")
#im = cv2.imread("mountain1.jpg")
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)#cv2.imread("mountain.jpg", cv2.IMREAD_GRAYSCALE)

ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(im, contours, -1, (0,255,0), 1)

cv2.imshow('image', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''