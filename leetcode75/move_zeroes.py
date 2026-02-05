"""
Move all the zeroes to the end of the list while maintaining order of the other elements.
do not create another list

We can use a two pointer at two ends. i for left and j for rigt.
if nums[i]!=0 we do nothing and move i to the right
if nums[i]=0 we swap nums i with nums[j]
then we move nums[j] to te left
but nums[j] could be zero too.
lets find a better solution

use i = 0 to keep track of the first 0, (and the last seen zero as we keep going) in the list
then we iterate through the array with a j
nums[j] is non zero then we can 
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
        
        
