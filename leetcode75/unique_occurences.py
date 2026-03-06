class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        """
        my approach is to:
        create a hash map that stores all values as well as their frequency
        if all frequencies are unique, return true, otherwise return false
        How would I check if all frequencies are unique?
        one way ik is to create an array of values, turn it to set, compare length of array
        and set, if same length then frequencies are unique.
        """
        hashmap = {}
        for item in arr:
            if item in hashmap:
                hashmap[item]+=1
            else:
                hashmap[item]=1
        if len(set(hashmap.values())) != len(set(arr)):
            return False
        return True
        
        