"""
Write a function smallerNumbersThanCurrent() that takes in a list of numbers nums as a parameter.
 For each nums[i], the function should find out how many numbers in the list are smaller than it. 
 (For each nums[i], count the number of valid j's such that j!=i and nums[j] < nums[i])

Return the answers in a list.

imma try to sort the list and return the number of items...nah sorting wont work cause 
i have to return it in the same order as it was before

chatgpt suggested:
create empty list
loop through original list
for each iteration, initialize counter to 0
loop thru each number and increase counter for every item < i
append the counter to list inside the loop
return list

lets try

"""
def smallerNumbersThanCurrent(nums):
    result = []
    for num1 in nums:
        counter = 0
        for num2 in nums:
            if num2 < num1:
                counter +=1
        result.append(counter)
    return result

#test case
nums = [6,1,2,2,3]
ans = smallerNumbersThanCurrent(nums)
print(ans)