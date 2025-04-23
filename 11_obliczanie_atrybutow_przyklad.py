class Model:

    def __init__(self, y_true, y_pred):

        Model._validate_input(y_true, 'y_true')
        Model._validate_input(y_pred, 'y_pred')

        if not len(y_true) == len(y_pred):
            raise ValueError('The y_true and y_pred objects must be of same '
                             'length.')

        self._y_true = y_true
        self._y_pred = y_pred
        self._accuracy = None

    def _validate_input(iters, var_name):
        if not isinstance(iters, (list, tuple)):
            raise TypeError(f'The {var_name} object must be of type list or '
                            f'tuple. Not {type(iters).__name__}.')

    def _validate_value(self, value, var_name):
        if not isinstance(value, (list, tuple)):
            raise TypeError(f'The value must be a list or tuple object. '
                            f'Not {type(value).__name__}.')

        mapping = {'y_true': '_y_pred', 'y_pred': '_y_true'}

        if not len(value) == len(getattr(self, mapping[var_name])):
            raise ValueError(f'The {var_name} object must be of length '
                             f'{len(getattr(self, mapping[var_name]))}.')

    @property
    def y_true(self):
        return self._y_true

    @y_true.setter
    def y_true(self, value):

        Model._validate_value(self, value, 'y_true')

        self._y_pred = value
        self._accuracy = None

    @y_true.deleter
    def y_true(self):
        print('deleting...')
        del self._y_true

    @property
    def y_pred(self):
        return self._y_pred

    @y_pred.setter
    def y_pred(self, value):

        Model._validate_value(self, value, 'y_pred')

        self._y_pred = value
        self._accuracy = None

    @y_pred.deleter
    def y_pred(self):
        print('deleting...')
        del self._y_pred

    @property
    def accuracy(self):
        if not self._accuracy:
            print('Calculating...')
            self._accuracy = sum([i == j
                                  for i, j in zip(self.y_true, self.y_pred)]) / len(self.y_true)
        print(f'Model accuracy: {self._accuracy:.4f}')


model = Model([0, 0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0])
