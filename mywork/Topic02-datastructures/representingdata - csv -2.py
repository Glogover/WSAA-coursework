# Modified program to calculate the average age by convertung the string that is read from the file into an integer and then doing the calculation

import csv
FILENAME= "data.csv"
#DATADIR = “where did you put it”

#with open (DATADIR + FILENAME, "rt") as fp:
with open (FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: # this is the first line, which contains the column names, we can skip it
            pass
        else: # all subsequent rows
            total += int(line[1]) # this is the second column, which contains the values we want to sum up, we need to convert it to an integer before adding it to the total
        linecount += 1 # this is a counter to keep track of how many lines we have read, we can use it to skip the first line and to print the total number of lines at the end
    print(f"Average age is {total/(linecount-1)}") # this is the average, we divide the total by the number of data lines, which is the total number of lines minus one for the header line