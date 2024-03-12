
import time


def timer(func):
    def wrapper(sec):
        start = time.time()
        func(sec)
        stop = time.time()
        print(f'Execution time: {stop - start:.4f}')
    return wrapper

@timer
def fake_sleep(sec):
    print(f'Executing {fake_sleep.__name__}...')
    time.sleep(sec)

fake_sleep(2)
fake_sleep(4)