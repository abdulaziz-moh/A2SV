# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rabbit, tortoise = head, head
        while rabbit and rabbit.next:
            tortoise = tortoise.next
            rabbit = rabbit.next.next
            if tortoise == rabbit:
                tortoise = head
                break
        else:
            return None
        while rabbit != tortoise:
            tortoise = tortoise.next
            rabbit = rabbit.next
        return rabbit