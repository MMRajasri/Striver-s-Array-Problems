# 'Coding_Ninja PRoblem' link--> https://www.codingninjas.com/studio/problems/ninja-and-the-sorted-check_6581957

def isSorted(n: int,  a: [int]) -> int:
    # Write your code here.
    c=0
    for i in range(1,n):
        if a[i]>=a[i-1]:
            continue
        c+=1
    if c!=0:
        return 0
    else:
        return 1
    pass
