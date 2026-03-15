class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node and node.next and node.next.next:
            node.val = node.next.val
            node = node.next
        node.val = node.next.val
        node.next = None