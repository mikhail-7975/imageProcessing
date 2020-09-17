# importing required libraries of opencv
import cv2
import numpy as np

# importing library for plotting
from matplotlib import pyplot as plt
print("enter alpha: ")
alpha = float(input())#0.5
print("enter beta: ")
beta = float(input())#0
#g(i, j) = a * g(i, j) + b

# reads an input image
img = cv2.imread('1234.jpg', 0)

for i in range(len(img)):
    for j in range(len(img[i])):
        img[i, j] = 255 if (alpha * img[i, j] + beta) > 255 else (0 if (alpha * img[i, j] + beta) < 0 else (alpha * img[i, j] + beta))

cv2.imshow('img', img)
cv2.waitKey(0)
# find frequency of pixels in range 0-255

hist,bins = np.histogram(img.flatten(),256,[0,256])

#cdf = hist.cumsum()
#cdf_normalized = cdf * hist.max()/ cdf.max()

#plt.plot(cdf_normalized, color = 'b')

plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imshow('res.png',res)
cv2.waitKey(0)

plt.hist(res.flatten(),256,[0,256], color = 'b')

plt.xlim([0,256])
plt.legend(('equ','histogram'), loc = 'upper left')
plt.show()
