"""
Given two strings s and sub, write a function count_substring() that returns the number of times 
the substring sub occurs in s. Occurrences should not overlap. A substring is a sequence of adjacent 
characters within a larger string.

Your solution must be recursive.

Evaluate the time complexity of your solution.
"""
def count_substrings(s, sub):
    if len(s)<len(sub):
        return 0
    if s[:len(sub)]==sub:
        return 1 + count_substrings(s[len(sub):], sub)
    else:
        return count_substrings(s[1:], sub)

s = "abcdeabcde"
sub = "abc"
print(count_substrings(s, sub))  # Output: 2
