class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        set1, set2 = set(nums1), set(nums2)
        return [list(set1-set2), list(set2-set1)]
#all i had to do was convert them to sets instead of doing all that
#still only beat 48% but i will move on to the next for now