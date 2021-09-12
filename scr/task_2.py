import time
import contextlib
import io
import inspect
from textwrap import indent

def decor_2(func_2):
    count = 0
    gap = 15
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        start = time.time()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            func_2(*args, **kwargs)
        end = time.time()
        dif = end - start
        print(f'{func_2.__name__} call {count} in {dif} sec')
        print()
        
        # 2 tipes of indentation were used: indent and {'': <n}
        # second is more convinient and it will be used later on
        
        print(  f'Name:  {indent(func_2.__name__, 8 * " ")} \n'
                f'Type:  {indent(str(type(func_2)), 8 * " ")} \n'
                f'Sign:  {indent(str(inspect.signature(func_2)), 8 * " ")}\n'
                f'{"Args:": <15}positional {args}\n'
                f'{"": <15}keyworded {kwargs}' )

        doc = indent(func_2.__doc__, gap * ' ')[gap:]
        print(f"{'Doc:': <15}{doc}")

        source = indent(inspect.getsource(func_2), gap * ' ')[gap:]
        print(f"{'Source:': <15}{source}")

        output = indent(f.getvalue(), gap * ' ')[gap:]
        print(f"{'Output:': <15}{output}\n")

    return wrapper 
