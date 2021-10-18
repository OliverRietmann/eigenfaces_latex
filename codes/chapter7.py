import numpy as np

from chapter5 import compute_coefficients

def distance(p, q, m, u_list):
    cp = compute_coefficients(p, m, u_list)
    cq = compute_coefficients(q, m, u_list)
    d = (cp - cq)
    return np.dot(d, d)


if __name__ == "__main__":

    import csv
    import os
    import sys

    import core.database as db
    import core.eigenfaces as ef
    import core.image as im

    # Get test data
    database_dir = str(sys.argv[1])
    image_list = [str(image) for image in sys.argv[2:]]

    # Get database and eigenfaces
    database = db.Database()
    database.load(database_dir, verbose=False)
    eigenfaces = ef.Eigenfaces()
    eigenfaces.load_database(database)
    m = eigenfaces.meanface

    # Write names into a list
    names_csv = os.path.join(database_dir, "names.csv")
    name_list = []
    with open(names_csv) as csvnames:
        for row in csv.reader(csvnames):
            name_list += [str(row[0])]

    # Compute distance to do classification
    c_list = [compute_coefficients(q, m, eigenfaces.U) for q in database.B]
    for image in image_list:
        p, resolution = im.load_image(image)
        c = compute_coefficients(p, m, eigenfaces.U)
        i = np.argmin([np.linalg.norm(c - c_tilde) for c_tilde in c_list])
        name = database.metadata[i][2]
        print(image, name)
