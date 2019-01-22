import os
import sys
import time
import numpy as np
import skimage.io
import cv2

# Download and install the Python COCO tools from https://github.com/waleedka/coco
# That's a fork from the original https://github.com/pdollar/coco with a bug
# fix for Python 3.
# I submitted a pull request https://github.com/cocodataset/cocoapi/pull/50
# If the PR is merged then use the original repo.
# Note: Edit PythonAPI/Makefile and replace "python" with "python3".
#  
# A quick one liner to install the library 
# !pip install git+https://github.com/waleedka/coco.git#subdirectory=PythonAPI

from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
from pycocotools import mask as maskUtils

import coco #a slightly modified version

from mrcnn.evaluate import build_coco_results, evaluate_coco
from mrcnn.dataset import MappingChallengeDataset
from mrcnn import visualize_cv


import zipfile
import urllib.request
import shutil
import glob
import tqdm
import random

ROOT_DIR = os.getcwd()

# Import Mask RCNN
sys.path.append(ROOT_DIR)  # To find local version of the library
from mrcnn.config import Config
from mrcnn import model as modellib, utils


PRETRAINED_MODEL_PATH = os.path.join(ROOT_DIR,"data/" "pretrained_weights.h5")
LOGS_DIRECTORY = os.path.join(ROOT_DIR, "logs")
MODEL_DIR = os.path.join(ROOT_DIR, "logs")
IMAGE_DIR = os.path.join(ROOT_DIR, "data", "test", "images-3-mod.jpg")

class InferenceConfig(coco.CocoConfig):
    # Set batch size to 1 since we'll be running inference on
    # one image at a time. Batch size = GPU_COUNT * IMAGES_PER_GPU
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1
    NUM_CLASSES = 1 + 1  # 1 Background + 1 Building
    IMAGE_MAX_DIM=320
    IMAGE_MIN_DIM=320
    NAME = "crowdai-mapping-challenge"
config = InferenceConfig()
config.display()

import keras.backend

K = keras.backend.backend()
if K=='tensorflow':
    keras.backend.set_image_dim_ordering('tf')

model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config)

model_path = PRETRAINED_MODEL_PATH

# or if you want to use the latest trained model, you can use : 
# model_path = model.find_last()[1]

model.load_weights(model_path, by_name=True)

class_names = ['BG', 'building'] # In our case, we have 1 class for the background, and 1 class for building

totalDetected = 0


files = glob.glob(os.path.join(IMAGE_DIR, "*.jpg"))
for n, file in enumerate(files):
  obj=os.path.basename(file)
  obj=obj[:-4]
  random_image = skimage.io.imread(file)
  predictions = model.detect([random_image]*config.BATCH_SIZE, verbose=1)
  p = predictions[0]
  img=visualize_cv.display_instances(random_image, p['rois'], p['masks'], p['class_ids'], class_names, p['scores'])
  #cv2.imshow('img', img)
  detected=len(p['rois'])
  totalDetected=totalDetected+detected
  detected=str(detected)
  n=n+1
  n=str(n)
  cv2.imwrite('result/'+obj+'_'+detected+'.jpg', img)
  #cv2.waitKey(0)
totalDetected=str(totalDetected)
f= open("result/total.txt","a+")
f.write(totalDetected)
f.write('\r\n')
f.close()
cv2.destroyAllWindows()

