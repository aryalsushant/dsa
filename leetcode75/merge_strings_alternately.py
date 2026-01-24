class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        #turn both string into lists
        #iterate thru the list and append items to result list alernating
        #if list 1 > list 2, append the index of list2's last item +1 
        # to the length of list1 to the resulting list, return as string

        lst1 = list(word1)
        lst2 = list(word2)
        result = []
        for i in range(min(len(lst1), len(lst2))):
            result.append(lst1[i])
            result.append(lst2[i])
        remaining_index=min(len(lst1), len(lst2))

        if len(lst1)>len(lst2):
            result.extend(lst1[remaining_index:])
        elif len(lst2)>len(lst1):
            result.extend(lst2[remaining_index:])
        return "".join(result)




        