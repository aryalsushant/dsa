"""
concetanate list basically. which means if you've given a list of length n, you return another list of length 2n where ans[i]
== nums[i] and ans[i+n]==nums[i+n]
"""

def concatenate_list(nums):
    ans = nums+nums
    return ans

print(concatenate_list([1,2,3,4]))