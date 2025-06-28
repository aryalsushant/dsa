"""
You are given a string s consisting of lowercase English letters, and are allowed to perform operations on it. 
In one operation, you can replace a character in s with another lowercase English letter.

Write a function make_palindrome() that takes in a string s and turns it into a palindrome with the minimum number
 of operations as possible. If there are multiple palindromes that can be made using the minimum number of operations, 
 make the lexicographically smallest one.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b 
differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b.

The function returns the resulting palindrome string.
"""
def make_palindrome(s):
    s_list =list(s)
    left, right = 0, len(s)-1

    while left<right:
        if s_list[left]!=s_list[right]:
            s_min = min(s_list[left], s_list[right])
            s_list[left] =s_list[right] = s_min
        left+=1
        right -=1
    return "".join(s_list)

#test case
s = "seven"
print(make_palindrome(s))