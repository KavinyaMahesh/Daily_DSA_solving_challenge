class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        # If the list is empty, make the new node the head
        if self.head is None:
            self.head = new_node
            return
        
        # Traverse to the last node
        temp = self.head
        while temp.next:
            temp = temp.next
            
        # Link the old tail and the new node
        temp.next = new_node
        new_node.prev = temp

def reverse_doubly_linked_list(head):
    current = head
    last = None
    
    # Swap next and prev pointers for all nodes
    while current is not None:
        last = current.prev
        current.prev = current.next
        current.next = last
        current = current.prev  # Moves to the next node because pointers swapped
        
    # Reset head to the new front node
    if last is not None:
        head = last.prev
    return head

if __name__ == "__main__":
    # Initialize the list manager
    dll = DoublyLinkedList()
    dll.insert_at_end(1)
    dll.insert_at_end(2)
    dll.insert_at_end(3)
    dll.insert_at_end(4)

    # Reverse the doubly linked list
    dll.head = reverse_doubly_linked_list(dll.head)

    # Print the reversed list: 4 3 2 1
    current = dll.head
    while current is not None:
        print(current.data, end=" ")
        current = current.next  
