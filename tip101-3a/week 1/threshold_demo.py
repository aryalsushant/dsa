"""
You are given a list of numbers and a threshold. Your goal is to return an array with numbers in the list that are
greater than the threshold.
"""

def above_threshold(lst, threshold):
    #step 1, initialize the list
    result = []

    #step 2, loop through each number
    for num in lst:

        #step 3, check if num is greater than threshold
        if num > threshold:

            #step 4, if num > threshold, add to new list
            result.append(num)

    #step 5, return new list
    return result

lst = [8,13,11,4,10,15]
threshold = 10

print(above_threshold(lst, threshold))

#what if list is empty?
empty = []
print(above_threshold(empty, threshold))

# so no need to write any additional code for this edge case :)
#also don't forget to talk through your process!!
