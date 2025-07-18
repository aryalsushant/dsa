def sqrt(x):
	if x<2:
		return x
	left = 0
	right = x
	while left<=right:
		middle = (left+right)//2
		square = middle*middle
		if square == x:
			return middle
		elif square < x:
			left = middle + 1
		else:
			right = middle - 1
	return right

print(sqrt(8))   # Expected: 2 (since sqrt(8) ≈ 2.828)
print(sqrt(9))   # Expected: 3
print(sqrt(15))  # Expected: 3
print(sqrt(16))  # Expected: 4
print(sqrt(1))   # Expected: 1

		
