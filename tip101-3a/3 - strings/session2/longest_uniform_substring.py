"""
Write a function longest_uniform_substring() that takes in a string s and returns the length of the longest
uniform substring. A uniform substring consists of a single repeated character.
1. create a hashmap
2. loop thru string
3. if character exists in hash, update its value by 1
4. if it doesn't, add it to hash with value 1
5. make a list of values, return the highest value
"""
def longest_uniform_substring(s):
    hash = {}
    for char in s:
        if char in hash:
            hash[char]+=1
        else:
            hash[char] =1
    return max(hash.values())

#test cases
s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2)