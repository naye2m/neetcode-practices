# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    @staticmethod
    def LN2L(ln:ListNode):
        l = [ln.val]
        c = 0
        while ln.next:
            c += 1
            if c > 20: return l
            ln = ln.next
            l.append(ln.val)
        return l
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if type(head) is not ListNode: return # Empty case
        if type(head.next) is not ListNode: return head # Empty case
        h0 = ListNode(head.val,head.next)
        h1 = h0.next
        h0.next = None
        h2:ListNode
        while h1.next:
            h2 = h1.next
            h1.next = h0
            
            h0 = h1
            h1 = h2
            h2 = h1.next
            # print(h0.val,h1.val,h2 and h2.val, self.LN2L(h0), self.LN2L(h1))
            if h2 == None:
                h1.next = h0
                return h1

        h1.next = h0
        return h1
