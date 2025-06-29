"""
The two-pointer approach can also be used with two pointers that iterate forward through a list or string at different 
rates. Use two pointers to solve the following problem:

Write a function squash_spaces() that takes in a string s as a parameter and returns a new string with each substring 
with consecutive spaces reduced to a single space. Assume s can contain leading or trailing spaces, but in the result 
should be trimmed.
Do not use any of the built-in trim methods.
"""
'''
def squash_spaces(s):
    result = []
    i = 0
    n = len(s)

    # Skip leading spaces
    while i < n and s[i] == ' ':
        i += 1

    while i < n:
        if s[i] != ' ':
            result.append(s[i])
        else:
            # Add only one space if the previous char wasn't a space
            if result and result[-1] != ' ':
                result.append(' ')
        i += 1

    # Remove trailing space if present
    if result and result[-1] == ' ':
        result.pop()

    return ''.join(result)
'''
def squash_spaces(s):
    result = []
    for i in range(0, len(s)):
        if s[i]!= " ":
            result.append(s[i])
        elif s[i] ==" " and s[i-1]!=" " and i>0:
            result.append(s[i])
       
    if result[-1] == " ":
        result.pop()
    return "".join(result)




print(squash_spaces("  hello    world  "))
print(squash_spaces("  what  about  this    ?"))
print(squash_spaces("this is my sentence"))