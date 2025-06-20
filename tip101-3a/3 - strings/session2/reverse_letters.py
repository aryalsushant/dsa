"""
Write a function reverse_only_letters() that takes in a string s as a parameter.
The function reverses the order of the letters in the string and returns the new string.
Non-letter characters should remain in their original positions.
"""

def reverse_only_letters(s):
    reverse = []
    
    
    # Step 1: Collect letters in reverse order
    for i in range(len(s)-1, -1, -1):
        if s[i].isalpha():
            reverse.append(s[i])

    result = []

    # Step 2: Build result, inserting reversed letters or keeping symbols
    for char in s:
        if char.isalpha():
            result.append(reverse.pop())  # Pop the next letter
        else:
            result.append(char)  # Keep symbol in same place
    return "".join(result)

    
   


   


            
    
   

  
#test case
s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)

