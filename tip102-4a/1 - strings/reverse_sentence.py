"""
Write a function reverse_sentence() that takes in a string sentence and returns the sentence with the 
order of the words reversed. The sentence will contain only alphabetic characters and spaces to separate 
the words. If there is only one word in the sentence, the function should return the original string.
"""
def reverse_sentence(sentence):
    lst = sentence.split()
    lst.reverse()
    return " ".join(lst)

# Test Case 1: Regular two-word sentence
print(reverse_sentence("hello world"))  
# Expected Output: "world hello"

# Test Case 2: Multiple words
print(reverse_sentence("the quick brown fox"))  
# Expected Output: "fox brown quick the"

# Test Case 3: Single word
print(reverse_sentence("Python"))  
# Expected Output: "Python"

# Test Case 4: Longer sentence
print(reverse_sentence("openai creates amazing tools"))  
# Expected Output: "tools amazing creates openai"

# Test Case 5: Sentence with extra spaces
print(reverse_sentence("  sky   is  blue  "))  
# Expected Output: "blue is sky"


