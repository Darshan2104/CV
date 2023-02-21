
import numpy
import cv2
from matplotlib import pyplot as plt
# ==============================================================================
# ==============================================================================
path = './3.jpeg'
# ==============================================================================
# ==============================================================================
#image1
img = cv2.imread(path)
plt.subplot(3, 2, 1), plt.imshow(img, 'gray')

blur = cv2.blur(img,(5,5))
gblur = cv2.GaussianBlur(img,(5,5),0)
median = cv2.medianBlur(img,5)

kernel = numpy.ones((5,5),numpy.uint8)
erosion = cv2.erode(median,kernel,iterations = 1)
dilation = cv2.dilate(erosion,kernel,iterations = 5)
closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)

edges = cv2.Canny(closing,9,420)

ret,threshold=cv2.threshold(edges.copy(),0,255,cv2.THRESH_BINARY)
contours,_=cv2.findContours(threshold,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
# contours = sorted(contours, key = cv2.contourArea, reverse = True) [:10]

cv2.drawContours(img,contours,-1,(0,0,255),2)
cv2.imshow("Show",img)

plt.subplot(3, 2, 2), plt.imshow(median, 'gray')
plt.subplot(3, 2, 3), plt.imshow(erosion, 'gray')
plt.subplot(3, 2, 4), plt.imshow(dilation, 'gray')
plt.subplot(3, 2, 5), plt.imshow(closing, 'gray')
plt.subplot(3, 2, 6), plt.imshow(edges, 'gray')

plt.show()

#to hold image
cv2.waitKey()