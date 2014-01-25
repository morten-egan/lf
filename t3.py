import cv2
import numpy as np
from matplotlib import pyplot as plt

gray = cv2.imread('images/res2.png',0)

ret,thresh = cv2.threshold(gray,127,255,1)
contours,h = cv2.findContours(thresh,1,2)

for cnt in contours:
	approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
	if len(approx) > 4:
		print "got one"