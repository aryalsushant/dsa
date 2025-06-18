"""
check if a sentence is a pangram i.e. contains every letter in the alphabet
return True or False
"""
def is_pangram(my_str):
    alphabet = "qwertyuiopasdfghjklzxcvbnm"
    my_str = my_str.lower()
    for i in alphabet:
        if i not in my_str:
            return False
    return True

#test case
my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))