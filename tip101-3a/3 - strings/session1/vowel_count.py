"""
Write a function vowel_count() that takes in a string s as a parameter and returns
 the number of vowels in the given string.
"""

def vowel_count(s):

    vowels = "AaEeIiOoUu"
    count = 0
    for char in s:
        if char in vowels:
            count +=1
    return count

#test case
my_str = "hello world"
my_str2 = "aAaAaAaAAA"
my_str3 = "ths strng s mssng vwls"

count1 = vowel_count(my_str)
print(count1)
count2 = vowel_count(my_str2)
print(count2)
count3 = vowel_count(my_str3)
print(count3)