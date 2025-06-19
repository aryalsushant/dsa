def first_unique_char(my_str):
    new = {}
    """
    create a new dictionary, loop through string
    if character in dictionary, update its value by 1
    if not, add it to dictionary with value 1

    then, loop through the range of length of string
    if dictionary[string[i]] is 1, return i
    outside the loop, as default, return -1
    if value is 1, return the key
    """
    for char in my_str:
        if char not in new:
            new[char] = 1
        else:
            new[char] += 1
        
    for i in range(len(my_str)):
            if new[my_str[i]]==1:
                return i
    return -1


#test cases
my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))