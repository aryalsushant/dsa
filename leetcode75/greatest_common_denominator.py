"""
in a string "abcabcabc" the greatest common denominator would be "abc" because the input string is just
abc repeated multiple times. in a string "leetcode" there is no greatest common denominatr.
I haven't done this problem before and idk how to start. i will have to look at the hint

"the greatest common denominator must be a prefix of each string so try all the prefixes"

actually we're given two strings, and we're supposed to return the greatest common denominator of both strings
this makes things simpler as we may be able to iterate through the strings and compare

so we can assume that the smaller string is the closest to being the result
what if smaller string is like "abab" and bigger is "ababab", we'd have to divide the smaller string into
parts to return "ab"

i thought about looping thru smaller string and comparing if each indice of it has the same character in bigger string
but that wont work for case str1="aaaaab" and str2 = "aaa". it would be a false positive.

ok so one method would be
find out how many times bigger string is bigger
if twice as big, split it into two
if both sides = smaller string, return smaller string
else return ""

only problem here is if the quotient of bigger/smaller is not a whole number
like if its 3/2
then we'd have to divide bigger /3
smaller /2
and return smaller/2 or bigger/3 if all parts of them are equal
otherwise return ""

problems: dividing a big string into multiple parts would be syntactically a nightmare
and space complexity would be too large

ok so the length of result would be the greatest common divisor of str1 and str2
if str1+str2!=str2+str1 then we can just return ""

but if its equal

we would find greatest common denominator of of length of two strings
that would be the length of the resulting string
then we can slice either string to that length and return it
"""
import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1+str2!=str2+str1:
            return ""
        else:
            len1 = len(str1)
            len2 = len(str2)
            g = math.gcd(len1, len2)
            return str1[:g]
        
# ideally i should use recursion instead of importing math, so i will definitely revisit this
# problem in the future