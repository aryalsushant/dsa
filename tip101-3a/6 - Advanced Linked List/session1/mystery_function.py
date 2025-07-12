class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

def mystery_function(head):
    if head is None:
        return None

    output_node = head.next
    if output_node is not None:
        output_node.prev = None
        head.next = None

    return output_node

def print_list(head):
    values = []
    current = head
    while current:
        values.append(str(current.value))
        current = current.next
    print(" <-> ".join(values))

# Build list: 1 <-> 2 <-> 3
head = Node(1)
second = Node(2)
third = Node(3)
head.next = second
second.prev = head
second.next = third
third.prev = second

# Call function
head = mystery_function(head)

# Print result
print_list(head)  # Output: 2 <-> 3
