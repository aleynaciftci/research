import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8') #uint8 basically an image, we're creating an empty image
#(500,500,3) (shape of width, height and the number of color channels)
cv.imshow('Blank', blank)

#img = cv.imread('Photos/cat.jpg') #this one is for drawing on a non-empty image
#cv.imshow('Cat', img)

#1.paint the image a certain colors
#blank[:] = 0,255,0 #green
#blank[:] = 0,0,255 #red
#cv.imshow('Green', blank)
#if you want to paint some portion ıf the image then you can give a range of pixels
#blank[200:300, 300:400] = 0,255,0
#cv.imshow('Green Square', blank)

#2.draw a rectangle
#cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
#cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=2)
#cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=cv.FILLED)
#cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=-1)
#cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
#cv.imshow('Rectangle', blank)

#3.draw a circle
#cv.circle(blank, (250,250), 40, (0,0,225), thickness=3)
#cv.imshow('Circle', blank)

#4.draw a line
#cv.line(blank, (100,150), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
#cv.imshow('Line', blank)

#5.write text
cv.putText(blank, 'Hello', (225,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)