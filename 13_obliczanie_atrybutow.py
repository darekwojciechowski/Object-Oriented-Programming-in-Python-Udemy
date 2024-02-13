class Model:

    def __init__(self, y_true, y_pred):
        self._y_true = y_true
        self._y_pred = y_pred
        self._accuracy = None

    @property
    def y_true(self):
        return self._y_true

    @y_true.setter
    def y_true(self, value):
        self._y_true = value
        self._accuracy = None

    @property
    def y_pred(self):
        return self._y_pred

    @y_pred.setter
    def y_pred(self, value):
        self._y_pred = value
        self._accuracy = None        

    @property
    def accuracy(self):
        if not self._accuracy:
            print('Calculating...')
            self._accuracy = sum([i == j
                for i, j in zip(self.y_true, self.y_pred)]) / len(self.y_true)
        print(f'Model accuracy: {self._accuracy:.4f}')

model = Model([0, 0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0])

model.accuracy
model.accuracy
model.y_true
model.y_true = [0, 0, 1, 0, 0, 1, 1]
model.__dict__
model.accuracy
model.y_pred
model.y_true = 'undefined'
model.accuracy

