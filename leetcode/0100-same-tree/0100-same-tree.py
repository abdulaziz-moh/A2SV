# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def traverse(p,q):
            if not p and not q:
                return True
            if (not p and q) or (not q and p):
                return False

            check = p.val == q.val
            return check and traverse(p.left, q.left) and traverse(p.right, q.right)
        return traverse(p,q)