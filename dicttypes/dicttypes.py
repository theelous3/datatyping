'''A module for ensuring your data's types conform to a specific mapping.'''

__all__ = ['validate_data']


class JsonTemplate:
    '''A little type validator class for Json.'''
    def __init__(self, structure):
        '''structure: dict - A dict of key/type pairs to check data against.'''
        self.structure = structure

    def __call__(self, test_dict, location=None):
        '''test_dict: dict - The dict whos types are to be checked, ya dummy.

        rtype: None'''
        if location is None:
            location = self.structure
        for s_key, s_value in location.items():
            if not isinstance(s_value, dict):
                try:
                    assert isinstance(test_dict[s_key], s_value)
                except AssertionError:
                    raise TypeError(
                        f'The value for "{s_key}" is not of type'
                        f' "{s_value.__name__}".'
                        f' It is "{type(test_dict[s_key]).__name__}"')
            else:
                self.__call__(test_dict[s_key], s_value)


def validate_data(structure, test_dict):
    awh_yeah = JsonTemplate(structure)
    awh_yeah(test_dict)
