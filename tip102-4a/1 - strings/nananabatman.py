"""
Problem 7: NaNaNa Batman!

Write a function nanana_batman() that accepts an integer x and prints the string 
"nanana batman!" where "na" is repeated x times. 
Do not use the * operator.

Examples:
Input: x = 6
Output: "nananananana batman!"

Input: x = 0
Output: "batman!"
"""
def nanana_batman(x):
    # loop from 0 to x, add a na everytime it increments, at the end print everything

    #what if x is negative
    if x<0:
        print("error")
    #but what if x is 0?
    elif x == 0:
        print("batman!")
    else:
        result = ""
        for i in range(x):
            result += "na"
            i +=1
        print(result +" batman!")

nanana_batman(3)
#edge case:
nanana_batman(0)
