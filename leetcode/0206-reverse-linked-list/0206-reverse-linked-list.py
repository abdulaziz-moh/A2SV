# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        forward, backward = head, head
        while backward and backward.next:
            backward = backward.next
        while forward != backward and backward.next != forward:
            forward.val, backward.val = backward.val, forward.val
            temp = forward
            while temp.next != backward:
                temp = temp.next
            backward = temp
            forward = forward.next
        return head
