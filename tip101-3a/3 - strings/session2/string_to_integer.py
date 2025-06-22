"""
Write a function string_to_integer_mapping() that takes in a string of digits s as a parameter and returns a 
list where each element is the integer value of the corresponding digit in the string.
"""
def string_to_integer_mapping(s):
    result = []
    for char in s:
        result.append(int(char))
    return result

#test case
s="12345"
print(string_to_integer_mapping(s))
