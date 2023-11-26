# 'Leet_Code' 1752. Check if Array Is Sorted and Rotated
"""Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation."""
#Link--> https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if nums==sorted(nums):
                return True
            nums = nums[1:]+[nums[0]]
        return False
        
