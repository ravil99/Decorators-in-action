import time
import contextlib
import io
import inspect
from textwrap import indent

class Decor_3:
    def __init__(self, func_3):
        self.__name__ = self
        self.calls = 0
        self.func_3 = func_3
        
    def __call__(self, *args, **kwargs):
        gap = 15
        self.calls += 1
        start = time.time()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            self.func_3(*args)
        end = time.time()
        dif = end - start
        with open(f"Decor_3_{self.func_3.__name__}{self.calls}.txt", "a") as file:
            file.write(f'{self.func_3.__name__} call {self.calls} in {dif} sec\n')

            file.write( f'Name:  {indent(self.func_3.__name__, 8 * " ")} \n'
                        f'Type:  {indent(str(type(self.func_3)), 8 * " ")} \n'
                        f'Sign:  {indent(str(inspect.signature(self.func_3)), 8 * " ")}\n'
                        f'{"Args:": <15}positional {args}\n'
                        f'{"": <15}keyworded {kwargs}\n')
            
            doc = indent(self.func_3.__doc__, gap * ' ')[gap:]
            file.write(f"{'Doc:': <15}{doc}\n")

            source = indent(inspect.getsource(self.func_3), gap * ' ')[gap:]
            file.write(f"{'Source:': <15}{source}\n")

            output = indent(f.getvalue(), gap * ' ')[gap:]
            file.write(f"{'Output:': <15}{output}\n")
    






            





   



        
       
 

