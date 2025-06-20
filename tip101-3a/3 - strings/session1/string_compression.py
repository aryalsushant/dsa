"""
Write a function that takes in a string my_str as a parameter and performs basic string compression using counts of 
repeated characters.

For example, the string "aabcccccaaa" would become "a2b1c5a3". If the compressed string does not become smaller than 
the original string, return the original string. Assume the string only has alphabetic characters.

step1: create a empty list and a variable
step2: loop through the string starting from the second character
step3: compare it with the previous character
step4: if they are equal, increment count by one
step5: if they are not equal, append it to the list with its count as the same string eg: a2
step6: at the end, we need to append the last character and its count. 
step7; and then, we will return the list as a single string using join, but only if its length is less than
that of the original string. if its not, just return the original string instead
"""
def compress_string(my_str):
    list = []
    count = 1

    for i in range(1, len(my_str)):
        if my_str[i] == my_str[i-1]:
            count += 1
        else:
            list.append(my_str[i-1]+str(count))
            count = 1
    list.append(my_str[-1] + str(count))

    if len(list) < len(my_str):
        return "".join(list)
    else:
        return my_str
        

#test case
my_str = "aaaaabbcccd"
compressed_Str = compress_string(my_str)
print(compressed_Str)

my_str2 = "abcde"
compressed_Str2 = compress_string(my_str2)
print(compressed_Str2)