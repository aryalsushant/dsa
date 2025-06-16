"""
take a list of integers and return the average of all numbers in it
"""

def average(scores):
    sum = 0
    divisor = len(scores)
    for num in scores:
        sum = num + sum
    return (sum / divisor)

scores = [84,73,92,95,88]
avg_score = average(scores)
print(avg_score)
    

