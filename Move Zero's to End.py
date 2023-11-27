# 'Coding_Ninja Problem' link--> https://www.codingninjas.com/studio/problems/ninja-and-the-zero-s_6581958

def moveZeros(n: int,  a: [int]) -> [int]:
    # Write your code here.
    anchor=0
    for explorer in range(n):
        if a[explorer]!=0:
            a[anchor], a[explorer] = a[explorer], a[anchor]
            anchor+=1
    return a
    pass
