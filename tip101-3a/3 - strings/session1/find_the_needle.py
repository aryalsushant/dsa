"""
Write a function find_the_needle() that takes in two string parameters: a needle and a haystack.
The function returns the index of the first occurrence of needle in haystack, or -1 if needle is 
not part of haystack.

so if i just had to find one character in the string and return the index of its first appearance,
i could do it but i dont know how to look for a substring. i need to fully understand the longest substring
problem first before i can start this
understood the longest substring problem by studying two pointers and sliding window technique, still dk how to
do this lol

slicing is what i need to use

oh ok i got it
so we loop thru the length of haystack-needle+1 bc at the length of haystack, we don't
have any characters at end to form a substring
then we slice the haystack from index i to i+length of the needle
if item at that index is equal to needle, return the index i
"""
def find_the_needle(haystack, needle):
    if needle == "":
        return 0
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1
    

#test cases
haystack = "tobeornottobe"
needle = "be"
print(find_the_needle(haystack, needle))

haystack2 = "leetcode"
needle2 = "leeto"
print(find_the_needle(haystack2, needle2))