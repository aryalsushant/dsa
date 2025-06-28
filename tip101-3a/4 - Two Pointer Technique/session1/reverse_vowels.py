"""
Write a function reverse_vowel() that takes in a string s as a parameter and returns a string with all the vowels
 in the string reversed. The consonants should remain in the same position. For this question, we consider a, e, i, o, 
 and u as vowels but not y. The vowels can appear in both lower and upper cases, more than once.
"""

def reverse_vowels(s):
    #lets try this the same way as move even integers
    s_list = list(s)
    left = 0
    right = len(s)-1
    vowels = ["A","E","I","O","U","a","e","i","o","u"]
    while left<right:
        if s_list[left] not in vowels:
            left +=1
        elif s_list[right] not in vowels:
            right -=1
        else:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left+=1
            right -=1
    return "".join(s_list)

#test case
s1 = "hello"
rev_s1 = reverse_vowels(s1)
print(rev_s1)

s2 = "leetcode"
rev_s2 = reverse_vowels(s2)
print(rev_s2)