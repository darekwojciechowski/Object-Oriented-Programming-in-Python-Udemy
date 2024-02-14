class Model:

    def __init__(self, y_true, y_pred):

        if not isinstance(y_true, (list, tuple)):
            raise TypeError(f'The y_true object must be of type list or tuple. '
                f'Not {type(y_true).__name__}.')
            
        if not isinstance(y_pred, (list, tuple)):
            raise TypeError(f'The y_pred object must be of type list or tuple. '
                f'Not {type(y_pred).__name__}.')   

        if not len(y_true) == len(y_pred):
            raise ValueError('The y_true and y_pred objects must be of same '
                'length.')         

        self._y_true = y_true
        self._y_pred = y_pred
        self._accuracy = None

    @property
    def y_true(self):
        return self._y_true

    @y_true.setter
    def y_true(self, value):
        if isinstance(value, (list, tuple)):
            if len(value) == len(self._y_pred):
                self._y_true = value
            else:
                raise ValueError(f'The y_true object must be of length '
                    f'{len(self._y_pred)}.')
        else:
            raise TypeError(f'The value must be a list or tuple object. '
                f'Not {type(value).__name__}.')
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
        if isinstance(value, (list, tuple)):
            if len(value) == len(self._y_pred):
                self._y_pred = value
            else:
                raise ValueError(f'The y_pred object must be of length '
                    f'{len(self._y_pred)}.')
        else:
            raise TypeError(f'The value must be a list or tuple object. '
                f'Not {type(value).__name__}.')
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

model.y_true
del model.y_true
model.__dict__