# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast:ListNode = head
        for i in range(n-1):
            fast=fast.next
        dummy = ListNode(-1)
        curr=dummy
        curr.next=head
        while(fast.next):
            fast=fast.next
            curr=curr.next
        curr.next=curr.next.next
        return dummy.next