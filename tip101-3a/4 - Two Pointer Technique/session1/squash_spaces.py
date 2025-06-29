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
    #created an empty list to store result
    result = []
    #looping from 0 to length of s.
    for i in range(len(s)):
        #if the character is not space, we append it
        if s[i]!= " ":
            result.append(s[i])
        #if the character is space but previous character is not space, we append that space
        #for character at index 0, s[i-1] will be the last character i.e. s[0-1] or s[-1]
        #so, we add one of the conditions is that i!=0 or i>0
        elif s[i] ==" " and s[i-1]!=" " and i>0:
            result.append(s[i])
    #at the end, if the last character is a space, we remove it
    if result[-1] == " ":
        result.pop()
    #convert the resulting array into a string and return it
    #ppl gonna think this is Ai generated because of well formatted code but no this is just how I work sometimes lol
    return "".join(result)




print(squash_spaces("  hello    world  "))
print(squash_spaces("  what  about  this    ?"))
print(squash_spaces("this is my sentence"))