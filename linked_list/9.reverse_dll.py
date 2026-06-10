class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def reverse_doubly_linked_list(head):
    current = head
    last = None
    
    while current is not None:
        # Swap the next and prev pointers
        last = current.prev
        current.prev = current.next
        current.next = last
        
        # Move to the next node (which is now stored in current.prev)
        current = current.prev
        
    # Check if the list was not empty and update head
    if last is not None:
        head = last.prev
        
    return head


# Example usage:
if __name__ == "__main__":
    # Create a doubly linked list: 1 <-> 2 <-> 3
    head = Node(1)
    second = Node(2)
    third = Node(3)

    head.next = second
    second.prev = head
    second.next = third
    third.prev = second

    # Reverse the doubly linked list
    head = reverse_doubly_linked_list(head)

    # Print the reversed list: should print 3, 2, 1
    current = head
    while current is not None:
        print(current.data, end=" ")
        current = current.next