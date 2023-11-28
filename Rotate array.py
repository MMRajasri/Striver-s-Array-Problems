# 'Codig_Ninja PRoblem' link--> https://www.codingninjas.com/studio/problems/rotate-array_1230543
def rotateArray(arr: list, k: int) -> list:
    # Write your code here.
    def reverse(start, end):
        while start<end:
            arr[start], arr[end] = arr[end], arr[start]
            start, end = start+1, end-1
        
    n=len(arr)
    reverse(0,n-1)
    #print(arr)
    reverse(0,n-k-1)
    #print(arr)
    reverse(n-k,n-1)
    #print(arr)
    return arr
    pass
