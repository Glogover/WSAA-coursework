# Reads in the iris data set as json
# Author: Marcin Kaminski

import json

FILENAME = "iris.json"
#DATADIR = "../../data/"
#FULLPATH = DATADIR + FILENAME
FULLPATH = FILENAME

with open(FULLPATH, "rt") as fp: # open the file for reading in text mode
    irisdataset = json.load(fp)    # this reads the json data from the file and converts it to a python object, in this case a list of dictionaries, each dictionary represents a row in the iris data set
    #print(irisdataset) # this is a python list of dictionaries, it is not json, you can tell because the keys are not in double quotes and the boolean value is capitalized
    print(irisdataset[0]) # this is the first row of the iris data set, it is a dictionary with keys "sepal_length", "sepal_width", "petal_length", "petal_width", and "species"