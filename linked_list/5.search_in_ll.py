class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def find(self, head,key):
        curr=head
        while curr is not None:
            if curr.data==key:
                return True
            curr=curr.next
        return False
    
    def print_list(self, head):
        temp=head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()


if __name__=="__main__":
    sol=Solution()

    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)
    print("original list:", end=" ")
    sol.print_list(head)

    key=3
    print(f"Is {key} present in the list?", sol.find(head,key))

    key=5
    print(f"Is {key} present in the list?", sol.find(head,key))

