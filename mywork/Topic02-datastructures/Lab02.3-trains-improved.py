# Python program that reads the XML from the URL and prints it out, using minidom.
# Author: Marcin Kaminski

import requests
import csv
from xml.dom.minidom import parseString

retrieveTags = [
    "TrainStatus",
    "TrainLatitude",
    "TrainLongitude",
    "TrainCode",
    "TrainDate",
    "PublicMessage",
    "Direction",
]

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
page.raise_for_status()  # fail fast if the request didn't work

doc = parseString(page.content)

# If you want to store the XML in a file (optional)
with open("trainxml.xml", "w", encoding="utf-8") as xmlfp:
    doc.writexml(xmlfp)

def get_text(parent, tag_name) -> str:
    """Safely get text content for a tag under parent; returns '' if missing/empty."""
    node = parent.getElementsByTagName(tag_name).item(0)
    if node is None or node.firstChild is None:
        return ""
    return node.firstChild.nodeValue.strip()

# Write tab-separated output (you used \t as delimiter)
with open("week03_train.csv", mode="w", newline="", encoding="utf-8") as train_file:
    train_writer = csv.writer(
        train_file,
        delimiter="\t",
        quotechar='"',
        quoting=csv.QUOTE_MINIMAL,
    )

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")

    for objTrainPositionsNode in objTrainPositionsNodes:
        dataList = [get_text(objTrainPositionsNode, tag) for tag in retrieveTags]

        # TrainCode is at index 3 in retrieveTags
        train_code = dataList[3]

        # Only write out DART trains
        if train_code.startswith("D"):
            train_writer.writerow(dataList)