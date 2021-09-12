import traceback
from datetime import datetime

import time
import contextlib
import io
import inspect
from textwrap import indent

def func_decor_4(func_4):
    count = 0
    gap = 15
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        start = time.time()
        try:
            with contextlib.redirect_stdout(io.StringIO()) as f:
                func_4(*args, **kwargs)
        except Exception:
            with open("log.txt", "a") as log:
                date = datetime. now(). strftime("%Y_%m_%d-%I:%M:%S_%p")
                log.write(f'{date}\n')
                traceback.print_exc(file=log)
                log.write(60*"-"+"\n")

        end = time.time()
        dif = end - start
        print(f'{func_4.__name__} call {count} in {dif} sec')
        print()
        
        # 2 tipes of indentation were used: indent and {'': <n}
        # second is more convinient and it will be used later on
        
        print(  f'Name:  {indent(func_4.__name__, 8 * " ")} \n'
                f'Type:  {indent(str(type(func_4)), 8 * " ")} \n'
                f'Sign:  {indent(str(inspect.signature(func_4)), 8 * " ")}\n'
                f'{"Args:": <15}positional {args}\n'
                f'{"": <15}keyworded {kwargs}' )

        doc = indent(func_4.__doc__, gap * ' ')[gap:]
        print(f"{'Doc:': <15}{doc}")

        source = indent(inspect.getsource(func_4), gap * ' ')[gap:]
        print(f"{'Source:': <15}{source}")

        output = indent(f.getvalue(), gap * ' ')[gap:]
        print(f"{'Output:': <15}{output}\n")

    return wrapper 

class Decor_4:
    def __init__(self, cl_func_4):
        self.__name__ = self
        self.calls = 0
        self.cl_func_4 = cl_func_4
        
    def __call__(self, *args, **kwargs):
        gap = 15
        try:
            with contextlib.redirect_stdout(io.StringIO()) as f:
                self.cl_func_4(*args)
        except Exception:
                with open("log.txt", "a") as log:
                    date = datetime. now(). strftime("%Y_%m_%d-%I:%M:%S_%p")
                    log.write(f'{date}\n')
                    traceback.print_exc(file=log)   
                    log.write(60*"-"+"\n")         
        self.calls += 1
        start = time.time()

        end = time.time()
        dif = end - start
        with open(f"Decor_4_{self.cl_func_4.__name__}{self.calls}.txt", "w") as file:
            file.write(f'{self.cl_func_4.__name__} call {self.calls} in {dif} sec\n')

            file.write( f'Name:  {indent(self.cl_func_4.__name__, 8 * " ")} \n'
                        f'Type:  {indent(str(type(self.cl_func_4)), 8 * " ")} \n'
                        f'Sign:  {indent(str(inspect.signature(self.cl_func_4)), 8 * " ")}\n'
                        f'{"Args:": <15}positional {args}\n'
                        f'{"": <15}keyworded {kwargs}\n')
            
            doc = indent(self.cl_func_4.__doc__, gap * ' ')[gap:]
            file.write(f"{'Doc:': <15}{doc}\n")

            source = indent(inspect.getsource(self.cl_func_4), gap * ' ')[gap:]
            file.write(f"{'Source:': <15}{source}\n")

            output = indent(f.getvalue(), gap * ' ')[gap:]
            file.write(f"{'Output:': <15}{output}\n")







    

        
