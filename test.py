'''Some lil tests.

This is a messy testing ground, please avert your eyes.'''

from numbers import Number
import json

from dicttypes import validate, create_structure

data_structure_1 = {
    "name": str,
    "age": int,
    "height": float,
    "favourite_things": {
        "cat": str,
        "flavour": str,
        "number": Number,
    },
    "list": [int, str, int]
}

#print(data_structure_1)

def test_fail():
    api_results = json.loads('{"name": "frank", "age": 999.2, "height":1.89, "favourite_things": {"cat": "ket", "flavour": "YUM", "number": 8}, "list": [1, 2, 3]}')
    try:
        validate(data_structure_1, api_results)
    except TypeError:
#        print("One passed.")
        ...


def test_pass():
    api_results = json.loads('{"name": "frank", "age": 999, "height":1.89, "favourite_things": {"cat": "ket", "flavour": "YUM", "number": 8}, "list": [1, "2", 3]}')
    validate(data_structure_1, api_results)
    print("Two passed.")


if __name__ == '__main__':
    test_fail()
    test_pass()

a = create_structure({'lol': 'wat', 'stuff': [1, 2, 3]}, strict=True)
