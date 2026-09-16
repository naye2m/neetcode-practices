# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    n=0

    def removeNthFromEnd(self, head: ListNode, n: int) -> Optional[ListNode]:
        self.n=n
        if n == 1 and type(head.next) is not ListNode: return head.next 
        if type(head.next.next) is not ListNode:
            if n ==1: return ListNode(val=head.val)
            else: return ListNode(val=head.next.val)
        
        try:
            ci = self.remove_elem(head)
            return head.next
        except:
            pass
        return head

    def remove_elem(self,n1) -> list[int]:
        if n1.next == None: return [1,n1]
        print("nii",self.n,n1.val )
        ci = self.remove_elem(n1.next)
        print("cii\t",ci[0],ci[1].val,self.n,n1.val )
        if ci[0] == self.n:
            n1.next = n1.next.next
            raise 
        return [ci[0] + 1, n1]

        


        

