"""
Write a function remove_char() that takes in a string s and an integer n as parameters, 
The function returns a new string with the nth character removed where 0 < n < len(s).
"""

def remove_char(s, n):
    result = ""
    for i in range(len(s)):
        if i != n:
            result += s[i]
    return result


#test case
s = "typpo"
fixed_s = remove_char(s, 2)
print(fixed_s)