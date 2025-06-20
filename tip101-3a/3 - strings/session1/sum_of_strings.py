"""
Write a function sum_of_number_strings() that takes in a list of strings nums. 
Each string is a representations of integers. The function should return the sum of these strings as an integer.
"""
def sum_of_number_strings(nums):
    sum = 0
    for num in nums:
        sum += int(num)
    return sum

#test case
nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)