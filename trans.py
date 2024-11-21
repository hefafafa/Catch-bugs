import cv2
import numpy as np

from os import walk
from os.path import join

def TransFile(folder):
    files = []
    for (dirpath, dirnames, filenames) in walk(folder):
        files.extend(filenames)
        break
    for file in files:
        if '.jpg' in file:
            Save_npy (folder, file, cv2.xfeatures2d.SIFT_create())



def Save_npy (folder, path, feature_detector):
    if path.endswith("npy"):
        return
    img = cv2.imread(join(folder, path),0)
    kp, descriptors = feature_detector.detectAndCompute(img, None)
    descriptor_file = path.replace(".jpg", ".npy")
    np.save(join(folder, descriptor_file), descriptors)
    

if __name__ == "__main__":
    folder = "FOLDER"######fill the FOLDER with images
    TransFile(folder)