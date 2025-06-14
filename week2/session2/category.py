"""
we are given a list of tuples
count how many times each item appears
return a dictionary that contains the category and the count
"""
def count_by_category(items):
    #1 create an empty dictionary
    counts = {}
    #2 loop through each tuple
    for category, _ in items:
        #3 if the category is in a dictionary, increment count
        if category in counts:
            counts[category]+=1
        #else, add category to dictionary with the value of 1
        else:
            counts[category] = 1
    #return the dictionary
    return counts