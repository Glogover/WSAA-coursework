import requests

#url = "http://google.com"
url = "http://andrewbeatty1.pythonanywhere.com/books"

def readbooks():
    response = requests.get(url)
    # we could do checking for correct response code here
    return response.json()

def readbook(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    # we could do checking for correct response code here 
    return response.json()

def createbook(book):
    response = requests.post(url, json=book)
    # should check we have the correct status code
    return response.json()

def updatebook(id, book):
     puturl = url + "/" + str(id)
     response = requests.put(puturl, json=book) 
     return response.json()

def deletebook(id):
    deleteurl = url + "/" + str(id) 
    response = requests.delete(deleteurl) 
    return response.json()

if __name__ == "__main__":

    book = {
    "author":"test",
    "title":"test title",
    "price":12345
    }

    #print(readbooks())
    #print(readbook(1694))
    #print(createbook(book))
    #print(updatebook(1694, book))
    print(deletebook(1694))

#print(response.text)