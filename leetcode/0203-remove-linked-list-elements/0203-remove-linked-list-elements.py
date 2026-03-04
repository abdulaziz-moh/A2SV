# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = ListNode()
        ans = prev
        prev.next = head
        temp = head
        while temp:
            if temp.val == val:
                prev.next = temp.next
                temp.next = None
                del temp
                temp = prev.next
            else:
                prev = prev.next
                temp = temp.next
        head = ans.next
        return head


        