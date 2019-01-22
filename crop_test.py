import numpy as np
import imutils
import cv2
import argparse

def crop(image, size=300):
	img = cv2.imread(image)
	height, width, channels = img.shape
	x=width
	y=height
	x0=0
	y0=0
	cropSize=int(size)
	crop=[]

	while y0<y:
		while x0<x:
			cropped = img[y0:y0+cropSize , x0:x0+cropSize]
			name = str(y0)+str(x0)
			crop.append(cropped)
			#cv2.imwrite("crop/"+name+".jpg", cropped)
			x0=x0+cropSize
		x0=0
		y0=y0+cropSize

	#print(len(crop))
	return crop

