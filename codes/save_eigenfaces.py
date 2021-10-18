# python3 save_eigenfaces.py /userdata/SelectedCelebs/ /userdata/eigenfaces.dat
# 18:15.87elapsed 727%CPU

import sys

import core.database as db
import core.eigenfaces as ef

database_dir = str(sys.argv[1])
picklefile = str(sys.argv[2])

database = db.Database()
database.load(database_dir, verbose=True)

eigenfaces = ef.Eigenfaces()
eigenfaces.load_database(database)
eigenfaces.save_picklefile(picklefile)
