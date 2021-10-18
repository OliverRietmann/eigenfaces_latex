import pickle
import os
import numpy as np

def get_meanface(B):
    return np.sum(B, axis=0) / B.shape[0]

def get_difffaces(B, meanface):
    return np.array([b - meanface for b in B])

def svd(A):
    U, s, VT = np.linalg.svd(A.transpose(), full_matrices=False) # A
    return U.transpose(), s # VT

class Eigenfaces:
    def __init__(self, resolution=None, meanface=None, U=None, s=None):
        self.resolution = resolution
        self.meanface = meanface
        self.U = U
        self.s = s

    def load_database(self, database):
        self.resolution = database.resolution
        self.meanface = get_meanface(database.B)
        A = get_difffaces(database.B, self.meanface)
        self.U, self.s = svd(A)

    def save_picklefile(self, picklefile):
        if os.path.isfile(picklefile):
            raise FileExistsError("File {0} already exists".format(picklefile))
        with open(picklefile, 'wb') as f:
            pickle.dump(self.resolution, f)
            pickle.dump(self.meanface, f)
            pickle.dump(self.U, f)
            pickle.dump(self.s, f)
            #pickle.dump(VT, f)

    def load_picklefile(self, picklefile):
        if not os.path.isfile(picklefile):
            raise FileNotFoundError("File {0} does not exist".format(picklefile))
        with open(picklefile, 'rb') as f:
            self.resolution = pickle.load(f)
            self.meanface = pickle.load(f)
            self.U = pickle.load(f)
            self.s = pickle.load(f)
