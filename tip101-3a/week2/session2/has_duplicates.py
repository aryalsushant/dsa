def hasDuplicates(nums, k):
    hashmap = {}
    for num in nums:
        if num in hashmap:
            hashmap[num]+=1
        else:
            hashmap[num]=1
    if k in hashmap.keys():
        if hashmap[k] > 1:
            return True
        else:
            return False
    else:
        return False

    
#test case
nums = [5, 6, 8, 2, 6, 4, 9]
check1 = hasDuplicates(nums, 3)
print(check1)
check2 = hasDuplicates(nums, 6)
print(check2)