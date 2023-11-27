# 'Leet_Code' 283. Move Zeroes

"""Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]"""

# link ---> https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        anchor=0
        for explorer in range(len(nums)):
            if nums[explorer]!=0:
                nums[anchor], nums[explorer] = nums[explorer], nums[anchor]
                anchor+=1
        
