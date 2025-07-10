"""
Given the head of a singly linked list, return True if the values of the linked list are palindromic and 
False otherwise. Use the two-pointer technique in your solution.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.
"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_palindrome(head):
    # Step 1: Find the middle using slow and fast pointers
    slow = head
    fast = head
    #conditions: head and tail need to be the same
    #idea: reverse a linked list, if both original and reversed are same, its a palindrome
    #idea: turn it into normal list and do it, but that would defeat the purpose of this practise session