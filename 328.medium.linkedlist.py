# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            
            return head

        evens = []
        odds = []
        p = head
        stateOdd = True
        while p:
            if stateOdd:
                odds.append(p.val)
                p = p.next
                stateOdd = False
            else:
                evens.append(p.val)
                p = p.next
                stateOdd = True

        if head.val == evens[0]:
            res = evens + odds
        else:
            res = odds + evens
        
        p2 = head
        for val in res:
            p2.val = val
            p2 = p2.next

        return head
