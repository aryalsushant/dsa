"""
Eeyore has collected two piles of sticks to rebuild his house and needs to choose pairs of sticks whose 
lengths are the right proportion. Write a function good_pairs() that accepts two integer arrays pile1 and 
pile2 where each integer represents the length of a stick. The function also accepts a positive integer k. 
The function should return the number of good pairs.

A pair (i, j) is called good if pile1[i] is divisible by pile2[j] * k. Assume 0 <= i <= len(pile1) - 1 and 
0 <= j <= len(pile2) - 1
"""
def good_pairs(pile1, pile2, k):
	pass

#test case
pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
good_pairs(pile1, pile2, k) #5

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
good_pairs(pile1, pile2, k) #2