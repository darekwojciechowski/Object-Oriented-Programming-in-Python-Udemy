class Person:

    def __init__(self, input_str):
        items = input_str.split(' ')
        if len(items) > 1:
            self._name = items[0]
            self._surname = items[1]
        else:
            raise ValueError('The object cannot be created.')

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname


Person.__dict__

person = Person('Mark Twain')
person.__dict__
person.name, person.surname

# person = Person('Mark')
# person = Person('Mark-Twain')


class Person:

    def __init__(self, input_str):
        if Person._is_string_with_space(input_str):
            items = input_str.split(' ')
            if len(items) == 2:
                self._name = items[0]
                self._surname = items[1]
            else:
                raise ValueError('The object cannot be created.')
        else:
            raise ValueError('Please insert a space between your name and '
                             'surname.')

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @staticmethod
    def _is_string_with_space(input_str):
        return isinstance(input_str, str) and ' ' in input_str


Person.__dict__

person = Person('Mark Twain')
person.name, person.surname

person = Person('Mark_Twain')
person = Person(4)
person = Person('Mark Twain')
