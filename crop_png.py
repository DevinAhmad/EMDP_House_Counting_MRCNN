import numpy as np
import imutils
import cv2
import argparse



ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image")
ap.add_argument("-s", "--size", required = True,
	help = "Size of crop")

args = vars(ap.parse_args())
img = cv2.imread(args["image"], cv2.IMREAD_UNCHANGED)


height, width, channels = img.shape
x=width
y=height

x0=0
y0=0
cropSize=int(args["size"])
'''
cropped = img[1:1 , 30:30]
cropped = img[30:60 , 30:60]
cv2.imshow("img", cropped)
cv2.waitKey()
'''


while y0<y:
	while x0<x:
		cropped = img[y0:y0+cropSize , x0:x0+cropSize]
		name = str(y0)+str(x0)
		y1, x1, n =cropped.shape
		if y1 >= cropSize/2 and x1 >= cropSize/2:
			cv2.imwrite("crop/"+name+".png", cropped)
		x0=x0+cropSize
	x0=0
	y0=y0+cropSize

	



"""
cropped = image[30:120 , 240:335]
cv2.imwrite(x, cropped)
"""
