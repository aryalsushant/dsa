"""
Given an array of integers popularity_scores representing the popularity scores of songs in a music festival 
playlist, return the number of popular song pairs.

A pair (i, j) is called popular if the songs have the same popularity score and i < j.

Hint: number of pairs = (n x n-1)/2
"""
def num_popular_pairs(popularity_scores):
    dict = {}
    for score in popularity_scores:
        if score in dict:
            dict[score]+=1
        else:
            dict[score]=1
    total_pairs = 0
    for key, value in dict.items():
        total_pairs += value * (value-1)//2
    return total_pairs

#test case
popularity_scores1 = [1, 2, 3, 1, 1, 3]
popularity_scores2 = [1, 1, 1, 1]
popularity_scores3 = [1, 2, 3]

print(num_popular_pairs(popularity_scores1))
print(num_popular_pairs(popularity_scores2))
print(num_popular_pairs(popularity_scores3)) 