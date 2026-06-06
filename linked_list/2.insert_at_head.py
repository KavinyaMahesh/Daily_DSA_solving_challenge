class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class Solution:
    def insert_at_head(self,head,newdata):
        new_node=Node(newdata,head)
        return new_node


    def print_list(self, head):
        temp=head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()


if __name__=="__main__":
    sol=Solution()

    head=Node(2)
    head.next=Node(3)

    head= sol.insert_at_head(head,1)
    sol.print_list(head)

    head= sol.insert_at_head(head,0)
    sol.print_list(head)
                    