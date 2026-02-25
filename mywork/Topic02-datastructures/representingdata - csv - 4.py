# Modified program to calculate the average age by reading in the CSV file as a Dictionary object

import csv
FILENAME= "data.csv"
#DATADIR = “where did you put it”

#with open (DATADIR + FILENAME, "rt") as fp:
with open (FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter=",", quoting = csv.QUOTE_NONNUMERIC) # this tells the reader to treat all non-numeric values as strings and all numeric values as floats, which allows us to do the calculation without having to convert the values to integers first, and it also allows us to access the values in each row by using the column names as keys in a dictionary
    count = 0 # this is a counter to keep track of how many lines we have read, we can use it to skip the first line and to print the total number of lines at the end
    total = 0 # this is the sum of all the ages we have read in
    for line in reader:
            total += line['age'] # this is the second column, which contains the values we want to sum up, since we have set the quoting parameter to QUOTE_NONNUMERIC, the values in this column will be read in as floats, so we can add them to the total without having to convert them to integers first, and since we are using a DictReader, we can access the values in each row by using the column names as keys in a dictionary
            #print(line) # this is a dictionary, the keys are the column names and the values are the values in each row, since we have set the quoting parameter to QUOTE_NONNUMERIC, the values in this column will be read in as floats, so we can add them to the total without having to convert them to integers first 
            count += 1 
    print(f"Average age is {total/(count)}") # this is the average, we divide the total by the number of data lines, which is the total number of lines minus one for the header line