import cv2 as cv
#import matplotlib.pyplot as plt

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

#plt.imshow(img)
#plt.show()

#BGR to grayscale
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

#BGR to HSV 
#hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#cv.imshow('HSV', hsv)

#BGR tO L*a*b
#lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
#cv.imshow('LAB', lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

#plt.imshow(rgb)
#plt.show()

cv.waitKey(0)

#you can't convert grayscale to hsv / you can convert grayscale to bgr then bgr to hsv