'''Some lil tests.'''

from numbers import Number
import json

from dicttypes import validate

data_structure_1 = {
    "name": str,
    "age": int,
    "height": float,
    "favourite_things": {
        "cat": str,
        "flavour": str,
        "number": Number,
    }
}


def test_fail():
    api_results = json.loads('{"name": "frank", "age": 999.2, "height":1.89, "favourite_things": {"cat": "ket", "flavour": "YUM", "number": 8}}')
    try:
        validate(data_structure_1, api_results)
    except TypeError:
        return False
    else:
        return True


def test_pass():
    api_results = json.loads('{"name": "frank", "age": 999, "height":1.89, "favourite_things": {"cat": "ket", "flavour": "YUM", "number": 8}}')
    try:
        validate(data_structure_1, api_results)
    except TypeError:
        return False
    return True


if __name__ == '__main__':
    assert not test_fail()
    assert test_pass()
