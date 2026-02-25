# playing with json
# Author: Marcin Kaminski

import json
data = {            # this is a dictionary in python, it will be converted to json       
    "name": "joe",
    "age": 21,
    "student": True
}

with open ("silly.json", "w") as fp:
    json.dump(data, fp, indent=4) # indent = 4 - this is optional, it just makes the json file easier to read
jsonString = json.dumps(data) # this is the same as above but it creates a string in memory instead of writing to a file, you can use this if you want to send json over the network for example
print(data) # this is a python dictionary, it is not json, it just looks like json, you can tell because the keys are not in double quotes and the boolean value is capitalized
print(jsonString) # this is a json string, it is not a python dictionary, you can tell because the keys are in double quotes and the boolean value is lowercase
