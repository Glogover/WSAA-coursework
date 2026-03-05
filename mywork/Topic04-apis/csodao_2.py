import requests
import json


urlBeginning = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd = "/JSON-stat/2.0/en"

def getAllasFile(dataset):
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll(dataset)), file = fp)

def getAll(dataset):
    url = urlBeginning + dataset + urlEnd
    response = requests.get(url)
    return response.json()

def getFormattedAsFile(dataset):
    pass

def getFormatted(dataset):
    data = getAll(dataset)
    ids = data["id"]
    values = data["value"]
    dimensions = data["dimension"]
    sizes = data["size"]
    valuecount = 0
    result = 0

    for dim0 in range(0, sizes[0]): # loop through the first dimension
        currentId = ids[0]
        index = dimensions[currentId]["category"]["index"][dim0]
        label = dimensions[currentId]["category"]["label"][index]
        print(label)
        for dim1 in range(0, sizes[1]): # loop through the second dimension
            currentId = ids[1]
            index = dimensions[currentId]["category"]["index"][dim1]
            label = dimensions[currentId]["category"]["label"][index]
            print("\t",label)
            for dim2 in range(0, sizes[2]): # loop through the third dimension
                currentId = ids[2]
                index = dimensions[currentId]["category"]["index"][dim2]
                label = dimensions[currentId]["category"]["label"][index]
                print("\t\t",label)
                for dim3 in range(0, sizes[3]): # loop through the fourth dimension
                    currentId = ids[3]
                    index = dimensions[currentId]["category"]["index"][dim3]
                    label = dimensions[currentId]["category"]["label"][index]
                    print("\t\t\t",label, " ", values[valuecount])
                    valuecount+=1

        

if __name__ == "__main__":
    #getAllasFile("FP001")
    getFormatted("FP001")






    