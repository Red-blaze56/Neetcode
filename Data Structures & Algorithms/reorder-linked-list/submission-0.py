class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Split the list and reverse the second half
        second = self.reverse(slow.next)
        slow.next = None  # Sever the connection
        
        # 3. Merge the two halves
        first = head
        while second:
            # Save next pointers
            tmp1, tmp2 = first.next, second.next
            
            # Re-wire pointers
            first.next = second
            second.next = tmp1
            
            # Move pointers forward
            first = tmp1
            second = tmp2