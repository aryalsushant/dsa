"""
Write a function swap_ends() that accepts a string my_str as a parameter and
returns a new string where the first and last characters from my_str are swapped.

so we probably have to find the size of the string,
create a new string
index the last sub string and append, 
index the middle sub strings and append,
then index the first sub strings and append
lastly return the new string

nahh thats not it
string[-1] = last character
string[1:-1] = middle characters, starting from one ending before -1
string[0] = first character
add them together and rteurn it

test case: only one character
"""

def swap_ends(my_str):
    if len(my_str) <= 1:
        return my_str
    else:
        return my_str[-1] + my_str[1:-1] + my_str[0]

#test case
my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)
