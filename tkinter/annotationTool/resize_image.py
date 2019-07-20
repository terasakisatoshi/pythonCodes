from glob import glob
import os

import numpy as np
import skimage
from skimage import transform, io


def resize_img(targetdir):
    IMAGE_EXTENSION = ".JPG"
    files = glob(os.path.join(targetdir, "*" + IMAGE_EXTENSION))
    files += glob(os.path.join(targetdir, ("*" + IMAGE_EXTENSION).lower()))
    for file in files:
        img = skimage.io.imread(file)
        h, w, c = img.shape
        if w > h:
            resized = transform.resize(img, (300, 400), preserve_range=True)
        else:
            resized = transform.resize(img, (400, 300), preserve_range=True)
        resized = resized.astype(np.uint8)
        if not os.path.exists("resized"):
            os.mkdir("resized")
        name = os.path.splitext(os.path.basename(file))[0] + IMAGE_EXTENSION
        save_path = os.path.join("resized", name)
        skimage.io.imsave(save_path, resized)


def main():
    targetdir = "unclassified/"
    resize_img(targetdir)


if __name__ == '__main__':
    main()
