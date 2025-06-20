"""
Write a function reverse_sentence() that 
takes in a string sentence as a parameter and 
returns the string with the sentence but with the order of the 
words reversed. The sentence will only contain alphabetic characters and 
spaces to separate the words. If there is only one word in the sentence, the 
function returns the original string.
"""
def reverse_sentence(sentence):
    words = sentence.split()
    words.reverse()
    return " ".join(words)
    #dont use "", have a space between the quotes so that the words have one space between them

#test case
sentence = "I solemnly swear I am up to no good"
print(reverse_sentence(sentence))
