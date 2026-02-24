# Python program that reads the XML from the URL and prints it out, using minidom.
# Author: Marcin Kaminski

import requests
import csv
from xml.dom.minidom import parseString

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)
# check it works
#print(doc.toprettyxml()) # output to console, comment this out once you know it works

# if I want to store the xml in a file. You can comment this out later.
with open("trainxml.xml", "w") as xmlfp:
    doc.writexml(xmlfp)

objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
for objTrainPositionsNode in objTrainPositionsNodes:
    #traincodeNode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
    #traincode = traincodeNode.firstChild.nodeValue.strip()
    #print(traincode)
    trainlatitudeNode = objTrainPositionsNode.getElementsByTagName("TrainLatitude").item(0)
    trainlatitude = trainlatitudeNode.firstChild.nodeValue.strip()
    print(trainlatitude)


