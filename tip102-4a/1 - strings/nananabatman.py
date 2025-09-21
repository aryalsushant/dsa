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
    # loop from 0 to x, add a na everythine it increments, at the end print everything
    result = ""
    for i in range(x):
        result += "na"
        i +=1
    return result +" batman"

print(nanana_batman(3))
