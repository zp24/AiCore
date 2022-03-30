import json

dict = {"member #002":{"first name": "John", "last name": "Doe", "age": 34},
        "member #003":{"first name": "Elijah", "last name": "Baley", "age": 27},
        "member #001":{"first name": "Jane", "last name": "Doe", "age": 42}}

with open('data.json', 'w') as fp:
    json.dump(dict, fp,  indent=4) #indent prettifies layout (dictionary not on one line)

############
import json
from json import JSONEncoder
from uuid import UUID

#Dealing with no UUID serialization support in json
JSONEncoder_olddefault = JSONEncoder.default
def JSONEncoder_newdefault(self, o):
    if isinstance(o, UUID): return str(o)
    return JSONEncoder_olddefault(self, o)
JSONEncoder.default = JSONEncoder_newdefault

with open('data.json', 'w') as fp:
    json.dump(dict, fp,  indent=4)