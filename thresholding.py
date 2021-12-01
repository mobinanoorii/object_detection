import numpy as np
from skimage import filters
import skimage.io


def binary_image(path):
    image = skimage.io.imread(path)
    size = image.shape
    m = size[0]  # rows
    n = size[1]  # columns

    # Gray = R*0.299 + G*0.587 + B*0.114;
    def rgb2gray(rgb):
        return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])

    if len(image.shape) == 3:
        gray = rgb2gray(image)
    else:
        gray = np.reshape(image, (m, n, 1))

    val = filters.threshold_otsu(gray)

    gray.flags.writeable = True

    arr = np.zeros((m, n))

    print("Threshold:", val)
    
    for i in range(m):
        for j in range(n):
            if gray[i, j] > val:
                arr[i, j] = 0
            else:
                arr[i, j] = 1

    return m, n, arr
