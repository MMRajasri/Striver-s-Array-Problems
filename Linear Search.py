# 'Coding_ninja Problemm' link --> https://www.codingninjas.com/studio/problems/linear-search_6922070

def linearSearch(n: int, num: int, arr: [int]) -> int:
    # Write your code here.
    c=0
    for i in range(len(arr)):
        if arr[i]==num:
            c+=1
            return i
    if c==0:
        return -1
    pass
