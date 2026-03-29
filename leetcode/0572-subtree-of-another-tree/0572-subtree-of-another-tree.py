# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def traverse(p,q):
            if not p and not q:
                return True
            if (not p and q) or (not q and p):
                return False

            check = p.val == q.val
            return check and traverse(p.left, q.left) and traverse(p.right, q.right)

        return traverse(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)