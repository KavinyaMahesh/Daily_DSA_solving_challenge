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

    def delete_head(self):
        if self.head is None:
            return
        
        if self.head.next is None:
            self.head=None
            return
        
        self.head=self.head.next
        self.head.prev=None

    def delete_at_end(self):
        if self.head is None:
            return
        
        if self.head.next is None:
            self.head=None
            return
        
        temp=self.head
        while temp.next:
            temp=temp.next
        
        temp.prev.next=None    


if __name__=="__main__":
    dll=DoublyLinkedList()
    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)
    dll.insert_at_end(40)

    dll.delete_head()

    dll.delete_at_end()

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