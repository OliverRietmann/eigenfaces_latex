import csv
import pickle
import os
import numpy as np
from PIL import Image

def save_image(p, resolution, filename):
    assert(np.prod(resolution) == p.shape[0])
    face01 = np.clip(p, 0.0, 1.0)
    facematrix = (255 * face01).astype(np.uint8).reshape(resolution)
    Image.fromarray(facematrix).save(filename)

def load_image(filename):
    if not os.path.isfile(filename):
        raise FileNotFoundError("File {0} not found".format(filename))

    with Image.open(filename) as image:
        resolution = (image.size[1], image.size[0])
        facematrix = np.asarray(image)
        p = facematrix.reshape((np.prod(resolution),)) / 255.0

    return p, resolution
