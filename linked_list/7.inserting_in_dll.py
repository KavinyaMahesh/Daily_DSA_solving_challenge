class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        temp=self.head
        while temp.next:
            temp=temp.next  

        temp.next=new_node
        new_node.prev=temp

    def insert_at_beginning(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node


if __name__=="__main__":
    dll=DoublyLinkedList()
    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)

    dll.insert_at_beginning(5)
    dll.insert_at_beginning(7)


    #traversing forward
    temp=dll.head
    while temp:
        print(temp.data,end=" ")
        temp=temp.next

    print()

    #traversing backward
    temp=dll.head
    while temp.next:
        temp=temp.next
    
    while temp:
        print(temp.data,end=" ")
        temp=temp.prev