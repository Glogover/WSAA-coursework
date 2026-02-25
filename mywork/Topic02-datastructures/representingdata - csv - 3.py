# Modified program to calculate the average age by using the quote parameter of the csv.reader function to read in the values as floats instead of strings, which allows us to do the calculation without having to convert the values to integers first

import csv
FILENAME= "data.csv"
#DATADIR = “where did you put it”

#with open (DATADIR + FILENAME, "rt") as fp:
with open (FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",", quoting = csv.QUOTE_NONNUMERIC) # this tells the reader to treat all non-numeric values as strings and all numeric values as floats, which allows us to do the calculation without having to convert the values to integers first
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: # this is the first line, which contains the column names, we can skip it
            pass
        else: # all subsequent rows
            total += line[1] # this is the second column, which contains the values we want to sum up, since we have set the quoting parameter to QUOTE_NONNUMERIC, the values in this column will be read in as floats, so we can add them to the total without having to convert them to integers first
        
        linecount += 1 # this is a counter to keep track of how many lines we have read, we can use it to skip the first line and to print the total number of lines at the end
    print(f"Average age is {total/(linecount-1)}") # this is the average, we divide the total by the number of data lines, which is the total number of lines minus one for the header line