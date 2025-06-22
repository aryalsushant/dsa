"""
Write a function partition_labels() that takes in a string s as a parameter. s consists of lowercase letters and 
represents the order of characters as they appear in a document. The function partitions s into as many parts as 
possible so that each unique letter appears in at most one part, and returns a list of integers representing the size 
of these parts.


Example Usage:

s1 = "ababcbacadefegdehijhklij"
print(partition_label(s1))

s2 = "abcabcbadefffeda"
print(partition_label(s2))
Example Output:

# s1 partitioned into "ababcbaca", "defegde" and "hijhklij"
[9, 7, 8]
# s2 cannot be partitioned into more parts because of the "a" character at the end
[16]
"""
def partition_label(s):
    #loop through string
    #while string[i]!=

#test case
s1 = "ababcbacadefegdehijhklij"
print(partition_label(s1))

s2 = "abcabcbadefffeda"
print(partition_label(s2))

