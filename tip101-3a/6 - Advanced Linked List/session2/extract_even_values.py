class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

def mystery_function(head):
    current = head
    output = []
    while current:
        if current.value % 2 == 0:
            output.append(current.value)
        current = current.next
    return output

# Create linked list: 1 -> 2 -> 3 -> 4
head = Node(1, Node(2, Node(3, Node(4))))

# Run function
output = mystery_function(head)
print(output)  # Output: [2, 4]
