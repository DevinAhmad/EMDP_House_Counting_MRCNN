import numpy as np
import imutils
import cv2
import argparse
import os
import glob

ROOT_DIR = os.getcwd()


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image folder")
ap.add_argument("-s", "--size", required = True,
	help = "Size of crop")

args = vars(ap.parse_args())

IMAGE_DIR = os.path.join(ROOT_DIR, args["image"])


cropSize=int(args["size"])
'''
cropped = img[1:1 , 30:30]
cropped = img[30:60 , 30:60]
cv2.imshow("img", cropped)
cv2.waitKey()
'''
files = glob.glob(os.path.join(IMAGE_DIR, "*.jpg"))
for n, file in enumerate(files):
	obj=os.path.basename(file)
	obj=obj[:-4]
	print(obj)
	img = cv2.imread(file)
	y, x, z= img.shape
	x0=0
	y0=0
	while y0<y:
		while x0<x:
			cropped = img[y0:y0+cropSize , x0:x0+cropSize]
			name = str(y0)+str(x0)
			y1, x1, n =cropped.shape
			n=str(n)
			if y1 >= cropSize/2 and x1 >= cropSize/2:
				cv2.imwrite("crop/"+obj+"_"+name+".jpg", cropped)
			x0=x0+cropSize
		x0=0
		y0=y0+cropSize

'''
while y0<y:
	while x0<x:
		cropped = img[y0:y0+cropSize , x0:x0+cropSize]
		name = str(y0)+str(x0)
		y1, x1, n =cropped.shape
		if y1 >= cropSize/2 and x1 >= cropSize/2:
			cv2.imwrite("crop/"+name+".jpg", cropped)
		x0=x0+cropSize
	x0=0
	y0=y0+cropSize
'''

	



