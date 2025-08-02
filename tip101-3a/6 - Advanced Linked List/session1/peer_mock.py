"""
given the head of two sorted ll, merge into one
function should return head
"""
#traverse through both lists
# if the value at list1 is lower, we would add that to the resulting list
# if else, add the value from list2
# return the head of the new list

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
def merge_linked_list(list1, list2):
    
    dummy_head = Node(0)
    current = dummy_head

    #while loop to traverse through the list
    while list1 and list2:
        if list1.value <= list2.value:
            #add the value as next
            current.next = list1
            list1 = list1.next
        else:
            #add value from list2 as next
            current.next = list2
            list2 = list2.next
        current = current.next
        
        #if there's leftovers in any list
    if list1:
        #add value from list1 to next
        current.next = list1
        list1 = list1.next
    elif list2:
        #add value from list2
        current.next = list2 #do not link values instead of the node
        list2 = list2.next
    return dummy_head.next

# --- Test Cases ---

# Helper function to print a linked list (for verification)
def print_linked_list(head):
    values = []
    temp = head
    while temp:
        values.append(temp.value)
        temp = temp.next
    print(values)

# Test Case 1: Basic merge
print("--- Test Case 1 ---")
list1_a = Node(1, Node(3, Node(5)))
list2_a = Node(2, Node(4, Node(6)))
print("List 1:", end=" ")
print_linked_list(list1_a)
print("List 2:", end=" ")
print_linked_list(list2_a)
merged_head_a = merge_linked_list(list1_a, list2_a)
print("Merged List (Expected: [1, 2, 3, 4, 5, 6]):", end=" ")
print_linked_list(merged_head_a)
print("-" * 20)

# Test Case 2: One list is empty
print("--- Test Case 2 ---")
list1_b = Node(10, Node(20, Node(30)))
list2_b = None
print("List 1:", end=" ")
print_linked_list(list1_b)
print("List 2: None")
merged_head_b = merge_linked_list(list1_b, list2_b)
print("Merged List (Expected: [10, 20, 30]):", end=" ")
print_linked_list(merged_head_b)
print("-" * 20)

# Test Case 3: Both lists are empty
print("--- Test Case 3 ---")
list1_c = None
list2_c = None
print("List 1: None")
print("List 2: None")
merged_head_c = merge_linked_list(list1_c, list2_c)
print("Merged List (Expected: []):", end=" ")
print_linked_list(merged_head_c)
print("-" * 20)

# Test Case 4: Elements with duplicates
print("--- Test Case 4 ---")
list1_d = Node(1, Node(2, Node(3)))
list2_d = Node(1, Node(2, Node(3)))
print("List 1:", end=" ")
print_linked_list(list1_d)
print("List 2:", end=" ")
print_linked_list(list2_d)
merged_head_d = merge_linked_list(list1_d, list2_d)
print("Merged List (Expected: [1, 1, 2, 2, 3, 3]):", end=" ")
print_linked_list(merged_head_d)
print("-" * 20)

# Test Case 5: Uneven length lists
print("--- Test Case 5 ---")
list1_e = Node(1, Node(5, Node(7, Node(9))))
list2_e = Node(2, Node(3))
print("List 1:", end=" ")
print_linked_list(list1_e)
print("List 2:", end=" ")
print_linked_list(list2_e)
merged_head_e = merge_linked_list(list1_e, list2_e)
print("Merged List (Expected: [1, 2, 3, 5, 7, 9]):", end=" ")
print_linked_list(merged_head_e)
print("-" * 20)

