# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        arr = []
        while temp:
            arr.append(temp.val)
            temp = temp.next
        stack = []
        for v in arr:
            while stack and stack[-1] < v:
                stack.pop()
            stack.append(v)
        head = ListNode()
        head.next = None
        temp = head
        for v in stack:
            newnode = ListNode()
            newnode.val = v
            newnode.next = None
            temp.next = newnode
            temp = temp.next
        return head.next
