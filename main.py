from thresholding import binary_image
from labeling import RecursiveConnectedComponentLabeler, RecursiveConnectedComponentLabeler2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import sys
import colors
import subprocess

sys.setrecursionlimit(1500000)


def transform_classes_to_colors(mat, row, col):
    colors_set = set()
    for i in range(row):
        for j in range(col):
            colors_set.add(mat[i, j])

    num_colors = len(colors_set)
    sample = colors.GetColors(min(num_colors, 25))
    correspond = {}
    curr = 0
    for c in colors_set:
        correspond[c] = sample[curr % 25]
        curr += 1

    rgb_array = np.zeros((row, col, 3), 'uint8')

    for i in range(row):
        for j in range(col):
            rgb_array[i, j] = correspond[mat[i, j]]
    return rgb_array


def max_color(mat, m, n):
    mx = -1
    for i in range(m):
        for j in range(n):
            mx = max(mx, mat[i,j])
    return str(int(mx))


def main():
    if len(sys.argv) == 1:
        path = "adidas.png"
    else:
        path = sys.argv[1]

    # m : rows - n : columns
    m, n, image = binary_image(path)

    label = RecursiveConnectedComponentLabeler().label_components(image)
    plt.figure(figsize=(30, 10))
    plt.subplot(1, 3, 1), plt.title('original')
    image_org = mpimg.imread(path)
    plt.imshow(image_org, cmap='gray'), plt.axis('off')
    plt.subplot(1, 3, 2), plt.title('gray')
    plt.imshow(image, cmap='binary'), plt.axis('off')
    plt.subplot(1, 3, 3), plt.title('label')
    plt.imshow(transform_classes_to_colors(label, m, n)), plt.axis('off')

    if (m < 20 and n < 20):
        fig, axs = plt.subplots(1, 1)
        int_array = label.astype(int)
        axs.axis('off')
        axs.set_aspect('equal')
        axs.table(cellText=int_array, loc='center', colWidths=[0.05] * n)

    plt.show()


if __name__ == "__main__":
    bashCommand = "rm -rf steps"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    process.communicate()
    bashCommand = "mkdir -p steps"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    process.communicate()
    main()
    exit()
