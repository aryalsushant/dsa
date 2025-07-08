"""
Write a function get_length() that takes in a node at an unknown position within a doubly linked list.
 The function should return the length of the entire list.
"""
class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

def get_length(node):
    #first go to the head of the list
    #then traverse through the list and increase counter by 1

    while node.prev:
        node = node.prev

    counter = 0
    current = node
    while current:
        current = current.next
        counter +=1
    return counter

#example test case
# 3 <-> 5 <-> 6 <-> 7
n7 = Node(7)
n6 = Node(6, next=n7)
n5 = Node(5, next=n6)
n3 = Node(3, next=n5)

n7.prev = n6
n6.prev = n5
n5.prev = n3

print(get_length(n6))  # Output: 4
#ok this test case works
