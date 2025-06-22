"""
Write a function binary_substrings_count() that takes in a string s representing a binary number as a parameter. 
The function counts the number of substrings that satisfy all of the following conditions:

contains an equal number of 0s and 1s
all the 0s in the substring are grouped consecutively
all the 1s in the substrings are grouped consecutively
"""
def binary_substrings_count(s):
    prev = 0
    curr = 1
    count = 0
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            curr +=1
        else:
            count += min(prev, curr)
            prev = curr
            curr = 1
    count += min(prev, curr)
    return count


#test case
s = "00110011"
print(binary_substrings_count(s))

s2 = "10101"
print(binary_substrings_count(s2))

s3 = "1111"
print(binary_substrings_count(s3))