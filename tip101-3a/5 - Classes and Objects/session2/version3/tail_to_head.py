"""
Write a function tail_to_head() that takes in the head of a linked list as a parameter, and moves the tail 
of the linked list to the front.
"""
#traverse through the linked list
#while current.next.next = Npne, current.next = head
#suppose 1,2,3,4,5, banauna parne 5,1,2,3,4 , 4.next.next = none, 4.mext.next = 1, 4.next = none

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def tail_to_head(head):
    current = head
    while current.next.next is not None:
        current = current.next
    last = current.next
    current.next = None
    last.next = head
    return last
