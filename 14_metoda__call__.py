class Doc:
    
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __call__(self):
        print(f'Wywołanie... {self}')

doc1 = Doc('OOP')
doc1

doc1()