"""
Given the head of a singly linked list, reverse the list, and return the reversed list. You must reverse
the list in place. Return the head of the reversed list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def reverse(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev.value
#test case
n1 = Node(1, Node(2, Node(3, Node(4))))

print(reverse(n1))  


