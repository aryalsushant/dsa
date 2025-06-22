"""
Write a function remove_vowels() that takes in a string s as a parameter and returns a new string with all the vowels 
removed. For the purposes of this exercise, consider a, e, i, o, and u as vowels and not y. The function should preserve 
the case of the original letters.
"""
def remove_vowels(s):
    vowels = "aeiou"
    result = ""
    for char in s:
        if char not in vowels:
            result += char
    return result

#test case
s = "Hello World"
new_string = remove_vowels(s)
print(new_string)
