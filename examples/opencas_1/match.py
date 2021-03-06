import sys
import matplotlib.pyplot as plt
import numpy as np
from time import time
sys.path.append('../../')
from SimpleSM.matching import StereoMatcher

# Importing Images and converting to gray scale
imgL = plt.imread('images/left.png')
imgL = np.dot(imgL[..., :], [.333, .333, .334])
imgR = plt.imread('images/right.png')
imgR = np.dot(imgR[..., :], [.333, .333, .334])

# Dynamic Programming
# Running the algorithm
matcher = StereoMatcher(imgL, imgR, method="dynamic_programming", occlusion_penalty=0, disparity_range=32)

# Computing main method + run time
start_time = time()
matcher.compute()
end_time = time()
print('Runtime for dynamic programming is: {} s'.format(end_time-start_time))

# Saving the image
disparity_map = matcher.get_disparity()
plt.imsave('dp.png', disparity_map, cmap=plt.get_cmap('jet'))

# Block Matching
# Running the algorithm
matcher = StereoMatcher(imgL, imgR, method="block_matching", disparity_range=32, kernel_size=5)

# Computing main method + run time
start_time = time()
matcher.compute()
end_time = time()
print('Runtime for block matching is: {} s'.format(end_time-start_time))

# Saving the image
disparity_map = matcher.get_disparity_image()
plt.imsave('bm.png', disparity_map, cmap=plt.get_cmap('jet'))
