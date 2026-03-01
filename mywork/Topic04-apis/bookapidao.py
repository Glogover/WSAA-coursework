# This is a module that provides a set of functions to interact with
# the demonstration book API hosted at PythonAnywhere. 

import requests
import json
url = "http://andrewbeatty1.pythonanywhere.com/books"

def getAllBooks():
    response = requests.get(url)
    return response.json()


