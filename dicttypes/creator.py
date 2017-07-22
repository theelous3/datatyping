#!/usr/bin/env python3


def create_structure(data):
    output = {}

    for key, value in data.items():
        if isinstance(value, dict):
            output[key] = create_structure(value)
        elif isinstance(value, list):
            if value:
                assert all(isinstance(item, type(value[0])) for item in value)
                output[key] = type(value[0])
            else:
                raise ValueError("Can't get the type of an empty list!")
        else:
            output[key] = type(value)
