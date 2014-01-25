import numpy as np
import cv2
 
im = cv2.imread('images/res.png')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)


kernel = np.ones((5,5),np.uint8)
# erosion = cv2.erode(imgray,kernel,iterations = 3)
closing = cv2.morphologyEx(imgray, cv2.MORPH_CLOSE, kernel)

ret,thresh = cv2.threshold(imgray,23,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print len(contours)

cv2.drawContours(im,contours,-1,(0,255,0),3)

# cv2.drawContours(im,[cnt],0,(255,0,0),-1)

cv2.imwrite('images/res5.png',im)