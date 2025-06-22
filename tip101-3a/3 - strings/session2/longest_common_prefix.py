"""
Write a function longest_common_prefix() that takes in a list of strings strings as a parameter.
 The function returns the longest common prefix (not substring) of all strings and if there are none,
   it returns an empty string "".
1. create new string
2. zip strings to create a tuple of characters
3. loop through list of list of characters
4. create a boolean and set it to true
5. loop through each character inside list of characters
6. if all characters not equal to first character, boolean is false and loop breaks
7. now outside the inner loop, if boolean is still true,
8. add first character to result
9. else break the loop
10. return result.

"""
def longest_common_prefix(strings):
    result = ""
    zipped = zip(*strings)
    for chars in zipped:
        all_match = True
        for char in chars:
            if char != chars[0]:
                all_match = False
                break
        if all_match:
            result += chars[0]
        else:
            break
    return result




#test case
strings = ["flower", "flow", "flight"]
common_string = longest_common_prefix(strings)
print(common_string)

strs = ["dog", "racecar", "car"]
common_str = longest_common_prefix(strs)
print(common_str)