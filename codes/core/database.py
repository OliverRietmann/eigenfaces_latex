import csv
import os

import numpy as np

import core.image as im

class Database:
    def __init__(self, resolution=None, B=None, metadata=None):
        self.resolution = resolution
        self.B = B
        self.metadata = metadata

    def load(self, directory, verbose=False):
        if not os.path.exists(directory):
            raise Exception("Input directory {0} does not exist.".format(directory))

        # Write names into a list
        names_csv = os.path.join(directory, "names.csv")
        if verbose: print("Read", names_csv)
        name_list = []
        male_list = []
        with open(names_csv) as csvnames:
            for row in csv.reader(csvnames):
                name_list += [str(row[0])]
                male_list += [int(row[1])]

        w_list = []
        resolution_list = []
        metadata = []
        for name, male in zip(name_list, male_list):
            if verbose: print("Processing", name)
            current_directory = os.path.join(directory, name)
            infofile = os.path.join(current_directory, "data.csv")
            with open(infofile) as info:
                imagefile_list = info.read().splitlines()
                filename_list = []
                v_list = []
                res_list = []
                for imagefile in imagefile_list:
                    filename = os.path.join(current_directory, imagefile)
                    v, res = im.load_image(filename)
                    filename_list += [filename]
                    v_list += [v]
                    res_list += [res]
            w_list += v_list
            resolution_list += res_list
            metadata += list(zip(filename_list, len(filename_list) * [male], len(filename_list) * [name]))

        assert(all(resolution == resolution_list[0] for resolution in resolution_list))

        B = np.array(w_list)

        self.resolution = resolution_list[0]
        self.metadata = metadata
        self.B = B

    def get_meanface(self):
        return np.sum(database.B, axis=0) / database.B.shape[0]

    def get_difffaces(self):
        meanface = self.get_meanface()
        return np.array([b - meanface for b in self.B])
