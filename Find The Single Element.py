# 'Coding_Ninja Prolem' link --> https://www.codingninjas.com/studio/problems/find-the-single-element_6680465

from typing import *

def getSingleElement(arr : List[int]) -> int:
    # Write your code here.
    for i in range(0,len(arr),2):
        if (i+1)>=len(arr) or arr[i]!=arr[i+1]:
            return arr[i]
    return -1
    pass
