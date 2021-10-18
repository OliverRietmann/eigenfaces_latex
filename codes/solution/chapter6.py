import numpy as np

from chapter5 import compute_coefficients

def compress(p, m, u_list, K_tilde):
    # Reduzierte Liste der ersten K_tilde Eigengesichter
    u_list_reduced = u_list[:K_tilde]
    c_list_reduced = compute_coefficients(p, m, u_list_reduced)
    a = np.zeros_like(p)
    for k in range(K_tilde)[::-1]:
        a += c_list_reduced[k] * u_list_reduced[k]
    return a + m


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
    for K_tilde in [20, 200, 2000]:
        q = compress(p, m, eigenfaces.U, K_tilde)
        filename = "./compress_{0}.png".format(K_tilde)
        im.save_image(q, resolution, filename)
