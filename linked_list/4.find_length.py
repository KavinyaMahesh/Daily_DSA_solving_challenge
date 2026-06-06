class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def find_length(self,head):
        count=0
        curr=head
        while curr is not None:
            count+=1
            curr=curr.next

        return count
    
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

    print("length of list:", sol.find_length(head))
