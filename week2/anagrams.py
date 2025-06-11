"""
given a list of strings words, group strings that are anagrams of each other
anagram = word formed by rearranging the letters
example: "eat" and "tea"

edge cases: what is words is empty? uppercase lowercase?

one way to do it?
we can sort the letters and count how many times a letter appears

sort the letters, then add the word to the dictionary with a value
the value is how many times it appears

lets write out the steps:
1. Make new dictionary
2. Loop through list
3. Sort letters
4. Add key with value 1 or increment key if its already there
5. Each key is gonna be set to a list

this is just flowing over my head tbh imma wait for her to write the code 
"""

def group_anagrams(words):
    #1 create an empty dictionary
    anagrams = {}
    #2 Loop through words
    for word in words:

        #3 sort the word to create a key
        key = "".join(sorted(word))
        #4 if key is not in dictionary, create a new list
        if key not in anagrams:
            anagrams[key]=[]
        #5 if it is in dictionary, add word to the group
        anagrams[key].append(word)
    #6 return the grouped list
    return list(anagrams.values())

words = ["bat", "tab", "tap", "pat", "cat", "act"]
print(group_anagrams(words))
