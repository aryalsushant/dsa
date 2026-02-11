class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #use two pointers to iterate from left side
        #only increase i if match, but always increase j
        # if i is length of smaller string, return true

        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
        return i == len(s)


        