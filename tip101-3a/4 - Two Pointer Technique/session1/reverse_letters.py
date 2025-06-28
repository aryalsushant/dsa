"""
Using the two-pointer approach, write a function reverse_only_letters() that takes in a string s as a parameter. 
The function reverses the order of the letters in the string and returns the new string. Non-letter characters should 
remain in their original positions.
"""
def reverse_only_letters(s):
    s_list = list(s)
    left = 0
    right = len(s_list)-1
    while left<right:
        if s_list[left].isalpha() and s_list[right].isalpha():
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left+=1
            right -=1
        elif s_list[left].isalpha()==False:
            left+=1
        elif s_list[right].isalpha()==False:
            right-=1
    return "".join(s_list)


#test case
s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)