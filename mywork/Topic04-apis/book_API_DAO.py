import requests
import json

url = "http://andrewbeatty1.pythonanywhere.com/books"

def getAllBooks():
    response = requests.get(url)
    return response.json()

def getBookById(id):
    geturl = url + "/" + str(id)
    response= requests.get(geturl)
    return response.json()

def createBook(book):

    response = requests.post(url, json=book)
    #headers = {"Content-Type": "application/json"}
    #response = requests.post(url, data=json.dumps(book), headers=headers)

    return response.json()

def updateBook(id, bookdiff):
    updateurl = url + "/" + str(id)
    response = requests.put(updateurl, json=bookdiff)
    return response.json()
    

def deleteBook(id):
    deleteturl = url + "/" + str(id)
    response= requests.delete(deleteturl)
    return response.json()


if __name__ == "__main__":
   """this is the main method, 
   it will only run if this file is run directly, 
   not if it is imported as a module """
   book = {
    "author":"test",
    "title":"test title",
    "price":123
    }
   bookdiff = {
    "price":1000000
    }

   #print(getAllBooks())
   #print(getBookById(1560))
   #print(deleteBook(77))
   #print(createBook({}))
   print(updateBook(1560, bookdiff))



          


