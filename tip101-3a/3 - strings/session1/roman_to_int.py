"""
Roman Numerals are represented by seven different symbols (I, V, X, L, C, D, and M) and have these corresponding values:

I = 1 V = 5
X = 10 L = 50
C = 100 D = 500
M = 1000

For example, 2 is written as II, which is just two ones added together.
12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for 4 is not IIII. Instead, the number 4 is written as IV.

Because the I is before the V, we subtract it to equal 4. The same principle applies to the number 9, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9
X can be placed before L (50) and C (100) to make 40 and 90
C can be placed before D (500) and M (1000) to make 400 and 900
Write a function roman_to_int() that takes in a string s that makes up a roman numeral. The function should return the integer value of s.
"""
def roman_to_int(s):
    roman = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value=0
    for char in reversed(s):
        value = roman[char]
        if value < prev_value: 
            total -= value
        else:
            total += value
            prev_value = value
    return total


#test cases
s = "XL"
print(roman_to_int(s))

s2 = "LVIII"
print(roman_to_int(s2))

s3 = "MCMXCIV"
print(roman_to_int(s3))

"""
so we create a dictionary of the roman characters and its corresponding value.
then, we loop through the string in reversed order
before that, we need two variables total and prev_value
for char in reversed[s],
if dict[s]<prev, value, we subtract it from total
else, we add it to total and make it equal to prev value
"""