"""
Write a function delete_minimum_elements(nums) that takes in a list of integers nums as a parameter and 
continuously removes the minimum element until the list is empty. The function returns a new list of all the 
elements in nums in the order in which they were removed.

I could use sort to return the result but thats not what the question is asking for
hint says use a while loop
im gonna try using a nested for loop first
nahh thats not gonna work
what if i use the min(function)?
oh yes i need a while loop to do that
"""
def delete_minimum_elements(nums):
    result = []
    while nums != []:
        min_val = min(nums)
        nums.remove(min_val)
        result.append(min_val)
    return result


#test case
nums = [5,3,2,8,3,1]
removed_lst = delete_minimum_elements(nums)
print(removed_lst)