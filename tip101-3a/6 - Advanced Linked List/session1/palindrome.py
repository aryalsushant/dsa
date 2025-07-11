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
    #multiple pass technique: use two pointers to find the middle of the list
    #reverse the second half of the list
    #compare if the first half and the second half is the same

    # Step 1: Find the middle using slow and fast pointers
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    #reverse the second half of the list
    prev = None
    current = slow
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    #check if the first half and second half are the same
    left = head
    right = prev
    while right:
        if left.value != right.value:
            return False
        left = left.next
        right = right.next
    return True

#test case
# 1 → 2 → 3 → 2 → 1
n5 = Node(1)
n4 = Node(2, n5)
n3 = Node(3, n4)
n2 = Node(2, n3)
n1 = Node(1, n2)

print(is_palindrome(n1))  # Output: True



