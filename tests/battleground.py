'''Some lil tests.
This is a messy testing ground, please avert your eyes, it
is bad times ahead my friend.'''

from numbers import Number
import json

from datatyping import validate, create_structure

data_structure_1 = {
    "name": str,
    "age": int,
    "height": float,
    "favourite_things": {
        "cat": str,
        "flavour": str,
        "number": Number,
    },
    "list": [[]]
}


api_results = json.loads('{"name": "frank", "age": 999, "height":1.89, "favourite_things":'
                         ' {"cat": "ket", "flavour": "YUM", "number": 8}, "list": []}')

if __name__ == '__main__':
    validate(data_structure_1, api_results)
