'''A module for ensuring your data's types conform to a specific mapping.

You may be thinking "wow, this type checking is extremely unpythonic". Good.
This whole exercise is unpythonic.'''

__all__ = ["validate"]


from array import array


_CONTAINERS = (list, tuple, array, dict)


def validate(structure, data, homogeneous=False):
    if isinstance(structure, dict):
        for k, v in structure.items():
            _struct_search(structure, data, homogeneous, k, v)
    elif isinstance(structure, (list, tuple, array)):
        for i, v in enumerate(structure):
            _struct_search(structure, data, homogeneous, i, v)


def _struct_search(structure, data, homogeneous,
                   lookup, cur_struct):
    # quick check to see we're not looking for missing data.
    # seems stupid but reduces complexity a fair bit
    try:
        data[lookup]
    except (IndexError, KeyError):
        raise LookupError('Data is missing from item with'
                          f' signature "{cur_struct}" -> {data}')

    if isinstance(cur_struct, dict):
            validate(cur_struct, data[lookup], homogeneous)

    elif isinstance(cur_struct, list):
        if homogeneous:
            try:
                assert len(cur_struct) == 1
            except AssertionError:
                raise ValueError(f'Provided too many items to homogeneous'
                                 f' structure "{cur_struct}"')
            item_type = cur_struct[0]
            if not all(isinstance(item, item_type) for item in data[lookup]):
                raise TypeError(
                    f'The types of the items of "{lookup}" are not all '
                    f' "{item_type.__name__}".'
                    f' They are {[type(item) for item in data[lookup]]}'
                )

        else:
            for x, value_structure in enumerate(cur_struct):
                try:
                    data[lookup][x]
                except IndexError:
                    raise IndexError(f'There are items missing from "{lookup}"')
                if not isinstance(value_structure, _CONTAINERS):
                    try:
                        assert value_structure == type(data[lookup][x])
                    except AssertionError:
                        raise TypeError(f'The types of the items of "{lookup}"'
                                        ' do not match the structure.')
                else:
                    validate(value_structure, data[lookup][x], homogeneous)

    elif not isinstance(data[lookup], cur_struct):
        raise TypeError(
            f'The value for "{lookup}" is not of type'
            f' "{cur_struct.__name__}".'
            f' It is "{type(data[lookup]).__name__}"'
        )
