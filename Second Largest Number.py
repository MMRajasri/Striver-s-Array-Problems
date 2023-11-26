# 'Coding_Ninja PRoblem' link--> https://www.codingninjas.com/studio/problems/ninja-and-the-second-order-elements_6581960

def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # Write your code here.
    l=[]
    a.sort(reverse=True)
    l.append(a[1])
    a.sort(reverse=False)
    l.append(a[1])
    return l
    pass
