"""
Write a function sort_list_by_parity() that takes in an integer list nums as a parameter and moves all the even
 integers at the beginning of the list followed by all the odd integers. The function returns any list that satisfies
   this condition.

   1. ok i just found out we can swap elements, lets do this
"""

def sort_array_by_parity(nums):
    left = 0
    right = len(nums)-1

    while left<right:

        if nums[left]%2 == 0:
            left+=1
        elif nums[right]%2 ==1:
            right ==1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1
    return nums
            
        

            
    
            
    
        

#test case
nums = [3,1,2,4]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))