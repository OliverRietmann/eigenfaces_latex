# python3 plot_eigenfaces.py /userdata/eigenfaces.dat eigenfaces/ 20
import sys
import os

import numpy as np

import core.eigenfaces as ef
import core.image as im

picklefile = str(sys.argv[1])
output_directory = str(sys.argv[2])

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

if len(sys.argv) == 4:
    truncate = int(sys.argv[3])
else:
    truncate = sys.maxint

eigenfaces = ef.Eigenfaces()
eigenfaces.load_picklefile(picklefile)

truncate = min(eigenfaces.U.shape[0], truncate)
digits = int(np.log10(truncate)) + 1
i = 0
for u, eigenvalue in zip(eigenfaces.U[:truncate], eigenfaces.s[:truncate]):
    p = u * np.sqrt(eigenvalue) * 0.5 + eigenfaces.meanface
    string_i = str(i).zfill(digits)
    filename = os.path.join(output_directory, "eigenface{0}.png".format(string_i))
    im.save_image(p, eigenfaces.resolution, filename)
    i += 1
