"""
returning the number of items in a list that are less than a threshold

1. Create empty list
2. iterate through original list
3. compare items in list to threshold, if less than threshold then add item to new list
4. return the length of the list
"""

def count_less_than(numbers, threshold):
    new_list = []
    for num in numbers:
        if num < threshold:
            new_list.append(num)
    return len(new_list)

numbers = [12,8,2,4,4,10]
threshold = 5
print(count_less_than(numbers, threshold))
