#this solution only beat 5% lol but imma save it anyway and will look for a better solution

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        res1, res2 = [], []
        for item in nums1:
            if item not in nums2 and item not in res1:
                res1.append(item)
        for item in nums2:
            if item not in nums1 and item not in res2:
                res2.append(item)
        answer = [res1, res2]
        return answer
        