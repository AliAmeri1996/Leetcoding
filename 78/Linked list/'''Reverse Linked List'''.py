'''Reverse Linked List'''
class Node:
    def __init__(self, value):
        self.value = value
        #This stores the given value in the node’s value attribute.
        self.next = None
        #This initializes the node’s next pointer to None, meaning:
        #Right now, the node does not point to any other node

def reverse_linked_list(head):
    prev = None #At the very start, there’s no previous node yet, so prev is None.
    current = head #is our traversal pointer.It starts at the head of the list and moves forward one node at a time
    
    while current:
        next_node = current.next  # store the next node
        current.next = prev       # reverse the link
        prev = current            # move prev forward
        current = next_node       # move current forward
    return prev  # new head

# Helper: print list
def print_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Example usage:
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print("Original list:")
print_list(head)

head = reverse_linked_list(head)

print("Reversed list:")
print_list(head)
