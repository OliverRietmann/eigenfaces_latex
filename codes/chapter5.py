import numpy as np

def compute_coefficients(p, m, u_list):
    K = len(u_list)
    c_list = np.zeros((K,))
    for k in range(K):
        c_list[k] = np.dot(u_list[k], p - m)
    return c_list


if __name__ == "__main__":

    import sys
    import copy

    import core.eigenfaces as ef
    import core.image as im

    p, resolution = im.load_image("./images/mona_lisa.png")
    M, N = resolution

    eigenfaces = ef.Eigenfaces()
    picklefile = str(sys.argv[1])
    eigenfaces.load_picklefile(picklefile)
    m = eigenfaces.meanface

    assert(resolution == eigenfaces.resolution)

    # Test compute_coefficients
    c_list = compute_coefficients(p, m, eigenfaces.U)
    q = c_list @ eigenfaces.U + m
    im.save_image(q, resolution, "./compute_coefficients.png")
