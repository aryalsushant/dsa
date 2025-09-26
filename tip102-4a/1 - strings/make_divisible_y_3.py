"""
Write a function make_divisible_by_3() that accepts an integer array nums. In one operation, 
you can add or subtract 1 from any element of nums. Return the minimum number of operations to make
 all elements of nums divisible by 3.

 plan: go thru all elements in list
 for each element, if i%3==0 no change, if i%3 == 1 i-1, if i%3 ==2 i+1
"""
def make_divisible_by_3(nums):
    count = 0
    for num in nums:
        if num%3==1 or num%3==2:
            count +=1
    return count

#test case
nums = [1, 2, 3, 4]
print(make_divisible_by_3(nums))

nums = [3, 6, 9]
print(make_divisible_by_3(nums))