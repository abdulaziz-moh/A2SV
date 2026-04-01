# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:

        count = 0
        def rec(root):
            nonlocal count
            if not root:
                return 0
            a = rec(root.left)
            b = rec(root.right)

            count += abs(a) + abs(b)
            root.val += (a + b)

            return root.val - 1
        rec(root)
        return count