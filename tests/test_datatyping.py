from numbers import Number

import pytest

from datatyping import validate


def test_basic_dict():
    assert not validate({"stuff": str},
                        {"stuff": "string"})


def test_basic_dict_fail():
    with pytest.raises(TypeError):
        validate({"stuff": int},
                 {"stuff": "string"})


def test_basic_list():
    assert not validate([int, int, int],
                        [1, 2, 3])


def test_basic_list_homog():
    assert not validate([[int]], [[1, 2, 3]], homogeneous=True)


def test_basic_list_fail():
    with pytest.raises(TypeError):
        validate([int, int, int],
                 [1, 2, "str"])


def test_basic_list_homog_fail_struct():
    with pytest.raises(ValueError):
        validate([[int, int]], [[1]], homogeneous=True)


def test_basic_list_homog_fail_data():
    with pytest.raises(TypeError):
        validate([[int]], [[1, "lol", 2]], homogeneous=True)


def test_basic_list_items_missing():
    with pytest.raises(IndexError):
        validate([[int, int, int]], [[1, 2]])


def test_basic_list_items_missmatch():
    with pytest.raises(TypeError):
        validate({"wat": [1, 2, 3]}, {"wat": [1, 2, '3']})


def test_basic_list_items_emptylist():
    with pytest.raises(IndexError):
        validate({"wat": [[]]}, {"wat": []})


def test_multi_basic_dict():
    struct = {"a": int,
              "b": list,
              "c": [int, int, str],
              "d": {"nested": int,
                    "stuff": int}
              }
    data = {"a": 1,
            "b": [5, 4, 3, 2, 1],
            "c": [1, 1, "x"],
            "d": {"nested": 1,
                  "stuff": 2}
            }
    assert not validate(struct, data)


def test_multi_basic_dict_fail_list():
    struct = {"b": list}
    data = {"b": "THIS FAILS"}
    with pytest.raises(TypeError):
        validate(struct, data)


def test_multi_basic_dict_fail_dict():
    struct = {"c": [int, int, str],
              "d": {"nested": int,
                    "stuff": int}
              }
    data = {"c": [1, 1, "x"],
            "d": {"nested": 1.23,
                  "stuff": 2}
            }
    with pytest.raises(TypeError):
        validate(struct, data)


def test_multi_basic_dict_partial():
    struct = {"d": {"nested": int,
                    "stuff": int}
              }
    data = {"d": {"nested": 1,
                  "stuff": 2},
            "undescribed": ["Can't", "Parse", "This",
                            "Dooo", "DoDoDo", "BaDo", "Badum"]
            }
    assert not validate(struct, data)


def test_wrong_container_list():
    struct = {"d": list}
    data = {"d": {}}
    with pytest.raises(TypeError):
        validate(struct, data)


def test_wrong_container_dict():
    struct = {"d": dict}
    data = {"d": list}
    with pytest.raises(TypeError):
        validate(struct, data)


def test_bad_signature():
    struct = {"d": int, "e": str}
    data = {"d": 1}
    with pytest.raises(LookupError):
        validate(struct, data)


def test_nested_list():
    struct = {"a": [int, int, [int]]}
    data = {"a": [1, 2, [3]]}
    assert not validate(struct, data)
