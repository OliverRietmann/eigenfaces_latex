import numpy as np

def meanface(b_list):
    K = len(b_list)
    return sum(b_list) / K

def difffaces(b_list):
    a_list = np.zeros_like(b_list)
    m = meanface(b_list)
    K = len(b_list)
    for k in range(K):
        a_list[k] = b_list[k] - m
    return a_list


if __name__ == "__main__":

    import sys

    import core.database as db
    import core.image as im

    database_dir = str(sys.argv[1])
    database = db.Database()
    database.load(database_dir, verbose=False)

    # Test meanface
    m = meanface(database.B)
    im.save_image(m, database.resolution, "./meanface.png")

    # Test diffface
    A = difffaces(database.B)
