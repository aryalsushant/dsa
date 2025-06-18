"""
reversing a string
so its just like reversing a list but
instead of using append you just add to a empty string using +=
"""
def reverse_string(my_str):
    reverse = ""
    for i in range(len(my_str)-1, -1, -1):
        reverse += my_str[i]
    return reverse

#test case
my_str = "live"
print(reverse_string(my_str))