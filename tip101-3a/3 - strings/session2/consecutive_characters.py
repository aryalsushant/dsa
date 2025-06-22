"""
Write a function count_consecutive_characters() that takes in a string str1 as a parameter and returns the count 
of the most frequent consecutive character.
"""
def count_consecutive_characters(str1):
    list_of_maximums=[]
    maximum_number = 1
    for i in range(1, len(str1)):
        if str1[i]==str1[i-1]:
            maximum_number +=1
        else: 
            maximum_number = 1
        list_of_maximums.append(maximum_number)
    return max(list_of_maximums)

        

#test case
str1 = "aaabbcaaaa"
count = count_consecutive_characters(str1)
print(count)
str2 = "abcde"
count2 = count_consecutive_characters(str2)
print(count2)