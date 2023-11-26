# "coding_ninja problem' link-->https://www.codingninjas.com/studio/problems/largest-element-in-the-array-largest-element-in-the-array_5026279
from sys import *
from collections import *
from math import *

def largestElement(arr: [], n: int) -> int:

    # Write your code from here.
    m=arr[0]
    for i in arr:
        if i>m:
            m=i
    return m
