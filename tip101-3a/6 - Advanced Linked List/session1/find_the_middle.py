"""
A variation of the two-pointer technique introduced in Unit 4 is to have a slow and a fast pointer that increment 
at different rates. Given the head of a linked list, use the slow-fast pointer technique to find the middle node of
 a linked list. If there are two middle nodes, return the second middle node.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why 
you believe your solution has the stated time and space complexity.
"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def find_middle_element(head):
    slow = head
    fast = head
    
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

head = Node(1, Node(2, Node(3, Node(4))))
head = find_middle_element(head)
print(head.value)

#time complexty: 0(n), bc we're using two pointers, but traversing only once
#space complexity: 01), bc we're not creating anything new
        
        