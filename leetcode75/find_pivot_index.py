class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        could just iterate through the range of length of array
        if sum of array[:i-1] = sum of array[i+1:]
        then return i
        if loop runs without ever meeting this condition then return -1

        """
        for i in range(len(nums)):
            #if sum(nums[:i-1]) == sum(nums[i+1:]):
            if sum(nums[:i]) == sum(nums[i+1:]): 
            #bc python slices are always inclusive on the left
                return i
        return -1
        