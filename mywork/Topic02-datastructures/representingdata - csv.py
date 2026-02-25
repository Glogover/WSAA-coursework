import csv
FILENAME= "data.csv"
#DATADIR = “where did you put it”

#with open (DATADIR + FILENAME, "rt") as fp:
with open (FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    for line in reader:
        if not linecount: # this is the first line, which contains the column names, we can skip it
            print(f"{line}\n----------------------")
        else: # this is a data line, we can print it
            print (line)
        linecount += 1 # this is a counter to keep track of how many lines we have read, we can use it to skip the first line and to print the total number of lines at the end