class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next or not head.next.next:
            return head
        first, second, odd = head, head.next, head.next

        while first and first.next and second and second.next:
            if first.next.next:
                first.next = second.next
                first = first.next
            if second.next.next:
                second.next = first.next
                second = second.next
        second.next = None 
        first.next = odd
        return head