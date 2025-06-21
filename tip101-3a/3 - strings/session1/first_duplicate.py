"""
Write a function first_repeated_char() that takes in a string s as a parameter and returns the index of the
first repeated character in the string. Uppercase and lowercase letters are considered different characters, 
and the function returns None if there are no repeated characters.
"""
def first_repeated_char(s):
    for i in range(len(s)):
        if s[i]==s[i-1]:
            return i
    return None

#test case
s = "hello world"
s2 = "aAbBCC"
s3 = "abcdefg"

print(first_repeated_char(s))
print(first_repeated_char(s2))
print(first_repeated_char(s3))