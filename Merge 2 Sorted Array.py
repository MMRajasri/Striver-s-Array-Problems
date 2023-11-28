# 'Coding_Ninja Problem' link --> https://www.codingninjas.com/studio/problems/sorted-array_6613259

def sortedArray(a: [int], b: [int]) -> [int]:
    # Write your code here
    u = list(set(a).union(set(b)))
    return sorted(u)
    
    pass
