'''A module for ensuring your data's types conform to a specific mapping.'''

__all__ = ["validate"]


def validate(structure, data, homogeneous=False):
    '''Validates data based on a template structure.

    structure: dict - A dict of {key: type} pairs to be used as a
        template to check the data against.
    data: dict - The data to be checked.

    rtype: None
    '''
    for key, value_structure in structure.items():
        if isinstance(value_structure, dict):
            validate(value_structure, data[key])
        elif isinstance(value_structure, list):
            # We want the other "elif" not to execute, so we nest the if
            # statements.
            # TODO: Implement more than just simple types for lists.
            if not isinstance(data[key], list):
                raise TypeError(
                    f'The value for "{key}" is not of type "list".'
                    f' It is "{type(data[key]).__name__}"'
                )

            if homogeneous:
                assert len(value_structure) == 1
                item_type = value_structure[0]
                if not all(isinstance(item, item_type) for item in data[key]):
                    raise TypeError(
                        f'The types of the items of "{key}" are not all '
                        f' "{item_type.__name__}".'
                        f' They are {[type(item) for item in data[key]]}'
                    )
            else:
                data_value_types = [type(v) for v in data[key]]
                print(data_value_types)
                print(value_structure)
                print(list(zip(value_structure, data_value_types)))
                try:
                    assert all(s == v for s, v in zip(value_structure,
                                                      data_value_types))
                except AssertionError:
                    raise TypeError(f'The types of the items of "{key}" do'
                                    f' not match the structure.')
        elif not isinstance(data[key], value_structure):
            raise TypeError(
                f'The value for "{key}" is not of type'
                f' "{value_structure.__name__}".'
                f' It is "{type(data[key]).__name__}"'
            )
