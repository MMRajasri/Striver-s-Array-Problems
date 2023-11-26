#'Coding_Ninja Problem' link--> https://www.codingninjas.com/studio/problems/left-rotate-an-array-by-one_5026278

from sys import *
from collections import *
from math import *

def rotateArray(arr: [], n: int) -> []:
    # Write your code from here.
    rev=arr[::-1]
    t=arr[1:]+[rev[-1]]
    return t
    pass

