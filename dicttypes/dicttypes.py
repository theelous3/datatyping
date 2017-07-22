'''A module for ensuring your data's types conform to a specific mapping.'''
import inspect

__all__ = ["validate"]


def validate(structure, data):
    for key, value_structure in structure.items():
        if isinstance(value_structure, dict):
            validate(value_structure, data[key])
        elif isinstance(value_structure, list):
            # We want the other "elif" not to execute, so we nest the if
            # statements.
            if not isinstance(data[key], list):
                raise TypeError(
                    f'The value for "{key}" is not of type "list".'
                    f' It is "{type(data[key]).__name__}"'
                )

            assert len(value_structure) == 1
            item_type = value_structure[0]
            if not all(isinstance(item, item_type) for item in data[key]):
                raise TypeError(
                    f'The types of the items of "{key}" are not all '
                    f' "{item_type.__name__}".'
                    f' They are {[type(item) for item in data[key]]}'
                )
        elif not isinstance(data[key], value_structure):
            assert inspect.isclass(value_structure)
            raise TypeError(
                f'The value for "{key}" is not of type'
                f' "{value_structure.__name__}".'
                f' It is "{type(data[key]).__name__}"'
            )
