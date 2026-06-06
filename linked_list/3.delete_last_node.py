class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Solution:
    def delete_last_node(self,head):
        if head is None or head.next is None:
            return None
        curr=head

        while curr.next.next is not None:
            curr=curr.next

        curr.next=None
        return head

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
    head=sol.delete_last_node(head)

    print("solution:", end=" ")
    sol.print_list(head)



