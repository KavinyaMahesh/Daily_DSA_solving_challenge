class Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.next=next
        self.prev=prev

if __name__=="__main__":
    head=Node(10)
    second=Node(20)
    third=Node(30)

    head.next=second
    second.prev=head
    second.next=third
    third.prev=second

    #traversing forward
    temp=head
    while temp:
        print(temp.data,end=" ")
        temp=temp.next

    print()

    #traversing backward
    temp=third
    while temp:
        print(temp.data,end=" ")
        temp=temp.prev        