from PIL import Image
import matplotlib.pyplot as plt
import cv2
import os
import itertools 
import numpy as np
import json

ROOT = os.path.dirname(os.path.abspath(__file__)) + '\\'
ACCESS_RIGHTS = 0o755
def assure_folder(fname, root = ROOT):
    if not os.path.exists(root + fname) :
        os.mkdir(root + fname, ACCESS_RIGHTS)

    
pack_folder = "C:\\Users\\Latitude\\Desktop\\GAN-CNN-sticker-generator\\packs\\aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaadeathaaaaaaaaaaaaaaaaaaa\\"

dataset_folder = ROOT + "datasets\\" + str(max([int(a) for a in os.listdir(ROOT + "datasets\\") if '.' not in a] + [0])) + "\\"
assure_folder(dataset_folder, '')

image_index = 0
for image_name in os.listdir(pack_folder) :
    img = cv2.imread(pack_folder + image_name)
    m = np.zeros((512, 512, 3))
    h, w = min([512, img.shape[0]]), min([512, img.shape[1]])  
    m[:h, :w] = img[:h, :w] 
    cv2.imwrite(dataset_folder + str(image_index) + ".jpg")
        
    image_index += 1   
    #plt.imshow(img)
    #plt.show()




