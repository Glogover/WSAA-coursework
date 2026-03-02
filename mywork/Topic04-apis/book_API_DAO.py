import requests
url = "http://andrewbeatty1.pythonanywhere.com/books"

def getAllBooks():
    response = requests.get(url)
    return response.json()

def getBookById(id):
    geturl = url + "/" + str(id)
    response= requests.get(geturl)
    return response.json()

def createBook(book):
    pass

if __name__ == "__main__":
    """this is the main method, 
    it will only run if this file is run directly, 
    not if it is imported as a module """
    #print(getAllBooks())
    print(getBookById(1560))
