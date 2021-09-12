import time
import contextlib
import io

def decor_1(func_1):
    count = 0
    def wrapper(*args):
        nonlocal count
        count += 1
        start = time.time()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            func_1(*args)
        end = time.time()
        dif = end - start
        print(f'{func_1.__name__} call {count} in {dif} sec')
    return wrapper 