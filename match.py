import cv2
import numpy as np

from os import walk
from os.path import join

query = cv2.imread("INPUT_IMAGE_NAME", 0)
folder = 'FOLDER'######fill the FOLDER with images
descriptors = []

for (dirpath, dirnames, filenames) in walk(folder):
    for file in filenames:
        if file.endswith("npy"):
            descriptors.append(file)
        print(descriptors)
        
        
sift = cv2.xfeatures2d.SIFT_create()
query_kp, query_des = sift.detectAndCompute(query, None)

index_params = dict(algorithm=0, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)

potential_culprints = {}
for d in  descriptors:
    matches = flann.knnMatch(query_des, np.load(join(folder, d)), k=2)
    good = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good.append(m)
            
    print ("img is %s ! matching rate is (%d)" % (d, len(good)))
    potential_culprints[d] = len(good)
    
max_matches = None
potential_suspect = None
for culprit, matches in potential_culprints.items():
    if max_matches == None or matches > max_matches:
        max_matches = matches
        potential_suspect = culprit
    
print("potential suspect is %s" % potential_suspect.replace("npy", "").upper())
