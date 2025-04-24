import cv2
import numpy as np
from rembg import remove
from PIL import Image
from transparent_background import Remover
import argparse
import os 
from datetime import datetime
def filename():
    os.makedirs("done",exist_ok=True)
    return "done/"+datetime.now().strftime("output_%Y%m%d_%H%M%S_%f")[:-3] + ".png"
 
# Load model
remover = Remover() # default setting
# remover = Remover(mode='fast', jit=True, device='cuda:0', ckpt='~/latest.pth') # custom setting
# remover = Remover(mode='base-nightly') # nightly release checkpoint
parse  = argparse.ArgumentParser()
parse.add_argument("image",help="input image",type=str)
arg = parse.parse_args()
# Usage for image
img = Image.open(arg.image).convert('RGB') # read image

out = remover.process(img) # default setting - transparent background

# out = remove(img,)

# out = remover.process(img)
# out = remover.process(img, type='rgba') # same as above
# out = remover.process(img, type='map') # object map only
# out = remover.process(img, type='green') # image matting - green screen
# out = remover.process(img, type='white') # change backround with white color
# out = remover.process(img, type=[0, 0, 0]) # change background with color code [255, 0, 0]
# out = remover.process(img, type='blur') # blur background
# out = remover.process(img, type='overlay') # overlay object map onto the image
# out = remover.process(img, type='samples/background.jpg') # use another image as a background
 
# out = remover.process(img, threshold=0.5) # use threhold parameter for hard prediction.

out.save(filename()) # save result

