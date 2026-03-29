# bookdao.py

import requests
import json

url = "http://127.0.0.1:5000/books"

def getAllBooks():
    response = requests.get(url)
    return response.json()

def getBookById(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()

def createBook(book):
    response = requests.post(url, json=book)
    return response.json()

def updateBook(id, bookdiff):
    updateurl = url + "/" + str(id)
    response = requests.put(updateurl, json=bookdiff)
    return response.json()

def deleteBook(id):
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()

if __name__ == "__main__":
    book = {
        'author': "test",
        'title': "test title",
        "price": 123
    }
    bookdiff = {
        "price": 1234444
    }
    #print(getAllBooks())
    #print(getBookById(1))
    print(createBook(book))
    #print(updateBook(1, bookdiff))
    #print(deleteBook(1))