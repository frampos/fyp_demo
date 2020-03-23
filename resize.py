# -*- coding: utf-8 -*-
import os
import glob
import cv2

#path of images to be resized
target_dir = "./images"

#path to save resized images
resized_dir = "./test"

extension = "jpg"

target_size = (350, 500)

#makes a list of paths of all possible files in the target_dir ending with the file extension defined earlier
path_to_target = glob.glob(os.path.join(target_dir, "*.{}".format(extension)))

#creates directory for resized images to be saved in
os.makedirs(resized_dir,exist_ok=True)

#iterates through each element (using enumerate) in the list made previously
for i, target in enumerate(path_to_target):

    #reads in the image
    img = cv2.imread(target)

    #resize image
    img_resized = cv2.resize(img, target_size)

    #concatenates new name for the resized image and the path for it to be saved in
    resized_name = os.path.join(resized_dir, "test_{}.{}".format(str(i+1), extension))

    #write resized image with new name in path
    cv2.imwrite(resized_name, img_resized)

