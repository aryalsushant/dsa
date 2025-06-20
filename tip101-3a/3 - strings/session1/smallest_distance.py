"""
Write a function min_distance() that takes in a list of strings words and two 
strings word1 and word2' as parameters. The function should return the minimum 
distance between word1 and word2 in the list of words. The distance between one 
word and an adjacent word in the list is 1.

we can create two  variables equal to 0
then we can loop through the words
and save the index of the two words to the variables
return the difference of two variables
"""
def min_distance(words, word1, word2):
    variable1 = -1
    variable2 = -1
    min_dist = len(words)
    for i in range(len(words)):
        if words[i] == word1:
            variable1 = i
        elif words[i] == word2:
            variable2 = i
    
    #its not correct to return here because there can be multiple distances
    #and if one distance is less than another, we need to replace it
        if variable1 != -1 and variable2 != -1:
            dist = abs(variable2-variable1)
            if dist < min_dist:
                min_dist = dist
    return min_dist



#test cases
words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)

