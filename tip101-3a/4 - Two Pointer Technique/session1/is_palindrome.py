"""
Write a function is_palindrome() that takes in a string s as a parameter and returns True if the string is a 
palindrome and False otherwise. You may assume the string contains only lowercase alphabetic characters.

The function must use the two-pointer approach, which is a common technique in which we initialize two variables
 (also called a pointer in this context) to track different indices or places in a list or string, then moves the 
 pointers to point at new indices based on certain conditions. In the most common variation of the two-pointer approach,
   we initialize one variable to point at the beginning of a list and a second variable/pointer to point at the end of
     list. We then shift the pointers to move inwards through the list towards each other, until our problem is solved or 
     the pointers reach the opposite ends of the list.
"""

def is_palindrome(s):
    left = 0
    right = len(s)-1
    palindrome = True
    while left<right:
        if s[left]!=s[right]:
            return False
            break
        left+=1
        right-=1
    return True


#test case
s = "amanaplanacanalpanama"
s2 = "helloworld"

print(is_palindrome(s))
print(is_palindrome(s2))