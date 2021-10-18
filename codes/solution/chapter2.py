import numpy as np

#---matrix_to_vector-begin---
def matrix_to_vector(P, M, N):
    v = np.zeros(M * N)
    for m in range(M):
        for n in range(N):
            v[n + N * m] = P[m, n]
    return v
#---matrix_to_vector-end---

def vector_to_matrix(v, M, N):
    P = np.zeros((M, N))
    for m in range(M):
        for n in range(N):
            P[m, n] = v[n + N * m]
    return P

def get_negative(p):
    MN = len(p)
    for i in range(MN):
        p[i] = 1.0 - p[i]
    return p


if __name__ == "__main__":

    import core.image as im

    p, resolution = im.load_image("./images/Diane_Kruger.png")
    M, N = resolution

    # Test vector_to_matrix
    P = vector_to_matrix(p, M, N)
    q = matrix_to_vector(P, M, N)
    im.save_image(p, resolution, "./vector_to_matrix.png")

    # Test get_negative
    q = get_negative(p)
    im.save_image(p, resolution, "./get_negative.png")
