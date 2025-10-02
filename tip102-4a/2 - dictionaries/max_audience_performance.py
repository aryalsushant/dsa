"""
You are given an array audiences consisting of positive integers representing the audience size for different
performances at a music festival.

Return the combined size of every audience that had the maxmium size.

The audience size of a performance is the number of people who attended that performance.
"""
def max_audience_performances(audiences):
    max_size = max(audiences)
    maxes = []
    for i in audiences:
        if i == max_size:
            maxes.append(i)
    return sum(maxes)

#test case
audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))