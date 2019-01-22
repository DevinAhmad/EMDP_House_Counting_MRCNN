import crop_test as ct 
import os
import glob
ROOT_DIR = os.getcwd()
IMAGE_DIR = os.path.join(ROOT_DIR, "data", "test", "images-blok-2a")
files = glob.glob(os.path.join(IMAGE_DIR, "*.jpg"))



crop=ct.crop(files[0])
for n in enumerate(crop):
	print(n)
