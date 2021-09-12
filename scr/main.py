import math
from time import time 
from task_1 import decor_1
from task_2 import decor_2
from task_3 import Decor_3
from task_4 import Decor_4, func_decor_4

# @decor_1 was "clued" to first 2 function in order to show it's functionality
@decor_1
def filtering_odds(k=[1,2]):
    """ Function filtering out odd numbers from the list.

    Positional arguments:
    k - list of numbers (ints or floats)
    """
    return list(filter(lambda n: n % 2 == 0, k))

@decor_1
def simple_dimple(l=1):
    """ This dummy function sums x + 1.

    Positional arguments:
    l - number(int or float)
    """
    return (lambda x: x+1)(l)

# Test for task_1
if __name__ == '__main__':
    print("_" * 25 + 'Test for task_1' + "_" * 25 + '\n')
    simple_dimple(2)
    print()
    simple_dimple(1)
    print()
    filtering_odds([1,3,4,6,8,10])
    print()
    filtering_odds([2,4,5,7,8,9])
    print('\n')

# These 4 functions will be used to test tasks 2-4
def equationroots( a=2, b=4, c=2): 
    """ This function solves the quadratic equation.
    
    Positional arguments:
    a - coefficient before x_squared
    b - coefficient before x
    c - free member
    """
    dis = b * b - 4 * a * c 
    sqrt_val = math.sqrt(abs(dis)) 

    if dis > 0: 
        print(" real and different roots ") 
        print((-b + sqrt_val)/(2 * a)) 
        print((-b - sqrt_val)/(2 * a)) 
      
    elif dis == 0: 
        print(" real and same roots") 
        print(-b / (2 * a)) 

    else:
        print("Complex Roots") 
        print(- b / (2 * a), " + i", sqrt_val) 
        print(- b / (2 * a), " - i", sqrt_val) 

def pascal_triangle(n=2):
    """Computes n rows of pascal_triangle.

    Positional argument:
    n - number final row to be computed
    """
    top = [1]
    app = [0]
    for i in range(n):
        print(top)
        print(list(zip(app + top, top + app)))
        top = [l+r for l,r in zip(app + top, top + app)]
    
def new_filtering_odds(k=[1,2]):
    """ Function filtering out odd numbers from the list.

    Positional arguments:
    k - list of numbers (ints or floats)
    """
    return list(filter(lambda n: n % 2 == 0, k))
    
def pop_it(l=1):
    """ This dummy function sums x + 1.

    Positional arguments:
    l - number(int or float)
    """
    return (lambda x: x+1)(l)


# Test for task_2
if __name__ == '__main__':
    print("_" * 25 + 'Test for task_2' + "_" * 25 + '\n')
    test_2_1 = decor_2(pascal_triangle)(2)
    test_2_2 = decor_2(equationroots)(3)


# Test for task_3
if __name__ == '__main__':
    print("_" * 25 + 'Test for task_3' + "_" * 25 + '\n')
    num = 0
# running Decor_3 and making table
    list_test_3 = [pascal_triangle, equationroots, new_filtering_odds, pop_it]
    test_3_time = {}
    for i in range(len(list_test_3)):
        start = time()
        test = Decor_3(list_test_3[i])()
        time_val = time() - start
        test_3_time.update({list_test_3[i] : time_val})
    new_l = sorted(test_3_time.items(), key = lambda x: x[1])
    print(f"{'Function':<20} {'|RANK':<20} {'|TIME ELAPSED'}")
    for k,v in (new_l):
        num += 1
        print(f"{k.__name__:<22}{num:<22}{v}")

# Test for task_4
if __name__ == '__main__':
        print("_" * 25 + 'Test for task_4' + "_" * 25 + '\n')
        # function decorator writes output to the terminal
        test_4_1 = func_decor_4(pascal_triangle)(2.5)
        test_4_2 = func_decor_4(pop_it)(1,2)

        # class decorator writes output to .txt file
        test_4_3 = Decor_4(equationroots)('a','b','c')
        test_4_4 = Decor_4(new_filtering_odds)(['a', 'b', 'c'])






        

























    