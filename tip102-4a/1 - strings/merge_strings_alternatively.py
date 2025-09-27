"""
Write a function merge_alternately() that accepts two strings word1 and word2. Merge the strings by 
adding letters in alternating order, starting with word1. If a string is longer than the other, append 
the additional letters onto the end of the merged string.

Return the merged string.
"""
def merge_alternately(word1, word2):
    min_length = min(len(word1), len(word2))
    result = []
    for i in range(min_length):
        result.append(word1[i])
        result.append(word2[i])
        i+=1
    if len(word1)>len(word2):
        for i in range(min_length, len(word1)):
            result.append(word1[i])
            i+=1
    elif len(word2)>len(word1):
        for i in range(min_length, len(word2)):
            result.append(word2[i])
            i+=1
    return "".join(result)

#test case
word1 = "wol"
word2 = "oze"
print(merge_alternately(word1, word2))

word1 = "hfa"
word2 = "eflump"
print(merge_alternately(word1, word2))

word1 = "eyre"
word2 = "eo"
print(merge_alternately(word1, word2))

