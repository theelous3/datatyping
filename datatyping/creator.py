'''The create_structure function takes a known sampling of good data and
constructs a type template for use with the validator, for type validation.
Whoopieeeee! Less typing!'''

__all__ = ['create_structure']


def create_structure(data, homogeneous=False):
    output = {}
    for key, value in data.items():
        if isinstance(value, dict):
            output[key] = create_structure(value)
        elif isinstance(value, list):
            if value:
                if homogeneous:
                    try:
                        assert all(isinstance(item, type(value[0]))
                                   for item in value)
                    except AssertionError:
                        raise TypeError("homogeneous assertion was enabled,"
                                        f" but '{key}' contains multiple types.")
                    output[key] = [type(value[0])]
                else:
                    output[key] = [type(v) for v in value]
            else:
                output[key] = list
        else:
            output[key] = type(value)
    return output
