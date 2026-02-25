""" This program reads in a JSON file from the internet and ouputs it as a Python object, 
in this case a dictionary, which we can then manipulate and access the data in it using 
the keys of the dictionary"""

import requests
url =" https://www.gov.uk/bank-holidays.json"
response = requests.get(url) # this sends a GET request to the specified URL and returns a response object, which contains the data that we requested from the server, in this case the JSON data from the bank holidays API
data = response.json()
#print(data)
print(data['northern-ireland']['events'][0]) # this is the first event in the northern ireland bank holidays, it is a dictionary with keys "title", "date", and "notes"