#   8_dekoratory

def pretty_print(func):
    def wrapper():
        print('=' * 30)
        func()
        print('=' * 30)
    return wrapper


@pretty_print
def hello():
    print('Python 3.8')


hello

hello()
