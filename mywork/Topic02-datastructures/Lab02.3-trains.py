# Python program that reads the XML from the URL and prints it out, using minidom.
# Author: Marcin Kaminski

import requests
import csv
from xml.dom.minidom import parseString

retrieveTags=['TrainStatus',
            'TrainLatitude',
            'TrainLongitude',
            'TrainCode',
            'TrainDate',
            'PublicMessage',
            'Direction'
            ]

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)
# check it works
#print(doc.toprettyxml()) # output to console, comment this out once you know it works

# if I want to store the xml in a file. You can comment this out later.
with open("trainxml.xml", "w") as xmlfp:
    doc.writexml(xmlfp)

# I had an issue with blank lines in the file so found solution at
# https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row
# adding the newline= '' parameter
with  open('week03_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")

    for objTrainPositionsNode in objTrainPositionsNodes:
       #traincodeNode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
       #traincode = traincodeNode.firstChild.nodeValue.strip()
       #print(traincode)

       #trainlatitudeNode = objTrainPositionsNode.getElementsByTagName("TrainLatitude").item(0)
       #trainlatitude = trainlatitudeNode.firstChild.nodeValue.strip()
       #print(trainlatitude)
       
       # now lets get everything
       dataList = []


       for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
            dataList.append(datanode.firstChild.nodeValue.strip())

        # instead of printing this you could output to another format
        #print (dataList)
        # for example a CSV file 
    #train_code = dataList[3] 
    #if train_code.startswith("D"): # only write out DART trains
            train_writer.writerow(dataList)


