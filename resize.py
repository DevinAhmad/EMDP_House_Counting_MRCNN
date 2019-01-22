import imutils
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])


resized = imutils.resize(image, width = 300, height = 300)

cv2.imshow("resized", resized)

cv2.imwrite("resized "+args["image"], resized)