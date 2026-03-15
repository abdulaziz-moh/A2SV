class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        prev, curr = None, head
        while curr:
            right = curr.next
            curr.next = prev
            prev = curr
            curr = right
        return prev