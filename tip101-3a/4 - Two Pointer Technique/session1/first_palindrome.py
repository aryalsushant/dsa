"""
Write a function first_palindrome() that takes in a list of strings words as a parameter and returns the first 
palindromic string in the list. A string is palindromic if it reads the same forward and backward. If there is no 
such string, return an empty string 
1. loop thru list
set a boolean to true
2. for each string, two pointers at each end
3. if left is not equal to right, boolean is false, break the while loop
4. if it is equal, move inward
5. if boolean is true, return word

"""

def first_palindrome(words):
    for word in words:
        left = 0
        right = len(word)-1
        is_palindrome = True

        while left<right:
            if word[left] != word[right]:
                is_palindrome = False
                break
            left+=1
            right -=1
        
        if is_palindrome:
            return word
    return ""

#test case
words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)