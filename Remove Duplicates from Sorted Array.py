#'Coding_Ninja' link--> https://www.codingninjas.com/studio/problems/remove-duplicates-from-sorted-array_1102307

def removeDuplicates(arr,n):
    # Write your code here.
    k={}
    for i in arr:
        if i not in k:
            k[i]=1
        else:
            k[i]+=1
    return len(k)
    pass
