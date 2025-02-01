# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # using two pointer, fast will iterate through linked list twice as fast as slow ptr
        
        if head.next is None:
            return None

        slow = fast = head

        prev = None # this pointer will hold state before the middle and will be used to skip the following value and be the return
        
        while fast and fast.next: # fast not out of bounds and not at the last node yet
            prev = slow
            fast = fast.next.next # travel twice as fast as slow pointer
            slow = slow.next

        prev.next = slow.next
        return head