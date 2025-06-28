"""
Write a function reverse_prefix() that takes in a 0-indexed string word and a character ch as parameters. 
The function reverses the segment of word that starts at index 0 and ends at the index of the first occurrence
 of ch (inclusive) and keeps the rest of the string the same. If ch does not exist in word, do nothing. Return the 
 resulting string.

 in simpler words, i need to swap the first occurence of ch with the character at index 0
"""
def reverse_prefix(word, ch):
    word_list = list(word)
    for i in range(len(word_list)):
        if word_list[i]==ch:
            word_list[0], word_list[i] = word_list[i], word_list[0]
            break
    return "".join(word_list)

#test case
word = "abcdefd"
rev_word = reverse_prefix(word, "d")
print(rev_word)

word2 = "helloworld"
rev_word2 = reverse_prefix(word2, "w")
print(rev_word2)

word3 = "xyzxyz"
rev_word3 = reverse_prefix(word3, "a")
print(rev_word3)