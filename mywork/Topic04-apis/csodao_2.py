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
    with open("cso-formatted.json", "wt") as fp:
        print(json.dumps(getFormatted(dataset)), file = fp)


def getFormatted(dataset):
    data = getAll(dataset)
    ids = data["id"]
    values = data["value"]
    dimensions = data["dimension"]
    sizes = data["size"]
    valuecount = 0
    result = {}
  

    for dim0 in range(0, sizes[0]): # loop through the first dimension
        currentId = ids[0]
        index = dimensions[currentId]["category"]["index"][dim0]
        label0 = dimensions[currentId]["category"]["label"][index]
        result[label0] = {}
      
        #print(label0)
        
        for dim1 in range(0, sizes[1]): # loop through the second dimension
            currentId = ids[1]
            index = dimensions[currentId]["category"]["index"][dim1]
            label1 = dimensions[currentId]["category"]["label"][index]
            result[label0][label1] = {}
           
            #print("\t",label1)
            
            for dim2 in range(0, sizes[2]): # loop through the third dimension
                currentId = ids[2]
                index = dimensions[currentId]["category"]["index"][dim2]
                label2 = dimensions[currentId]["category"]["label"][index]
                result[label0][label1][label2] = {}
               
                #print("\t\t",label2)
                
                for dim3 in range(0, sizes[3]): # loop through the fourth dimension
                    currentId = ids[3]
                    index = dimensions[currentId]["category"]["index"][dim3]
                    label3 = dimensions[currentId]["category"]["label"][index]
                    #print("\t\t\t",label, " ", values[valuecount])
                    result[label0][label1][label2][label3] = values[valuecount]   
                    valuecount+=1

    print(result)
    return result

if __name__ == "__main__":
    #getAllasFile("FP001")
    getFormattedAsFile("FP001")






    