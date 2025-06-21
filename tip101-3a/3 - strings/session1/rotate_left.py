"""
Write a function rotate_left() that takes in a string s and an integer n as parameters. 
The function returns a new string with the first n characters moved to the end of the string 
where 1 <= n <= len(str).
"""
def rotate_left(s, n):
    return s[n:]+s[:n]

#test case
s = "rotation"
print(rotate_left(s, 2))