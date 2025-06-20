"""
Write a function wordPattern() that takes in a string pattern and a string s as parameters.
The function returns True if s follows the pattern and False otherwise. The string follows 
the pattern if there is a 1:1 correspondence between a letter in the pattern and a non-empty word in s.

Example Usage:

pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s))
s2 = "dog cat cat fish"
print(wordPattern(pattern, s2))

pattern2 = "aaaa"
s3 = "dog cat dog cat"
print(wordPattern(pattern2, s3))
s4 = "dog dog dog dog"
print(wordPattern(pattern2, s4))
Example Output:

True
False
False
True
"""

def wordPattern(pattern, s):
    #1. split s into a list of words
    words = s.split()

    #2, if length of words != length of pattern, return false
    if len(words) != len(pattern):
        return False

    #3, create a char_t_word and word_to_char dictionaries
    char_to_word = {}
    word_to_char = {}

    #4 for each char, word in (pattern, words)
    for char, word in zip(pattern, words):


        #if character is in word dictionary, 
        if char in char_to_word:
        
            #if current mapping is not the word, return false
            if char_to_word[char] != word:
                return False
            
        #else:
        else:
            char_to_word[char] = word
            #add to dictionary
        #5 repeat 4 for words_to_char
        if word in word_to_char:
            if word_to_char[word] != char:
                return False
            else:
                word_to_char[word] = char

    #6. return True
    return True




#test cases
pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s))
s2 = "dog cat cat fish"
print(wordPattern(pattern, s2))

pattern2 = "aaaa"
s3 = "dog cat dog cat"
print(wordPattern(pattern2, s3))
s4 = "dog dog dog dog"
print(wordPattern(pattern2, s4))