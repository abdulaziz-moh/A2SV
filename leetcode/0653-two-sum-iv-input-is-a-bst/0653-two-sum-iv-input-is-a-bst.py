# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def bst(root, num):
            if not root:
                return False
            val = root.val
            return num == val or (bst(root.left, num) if num < val else bst(root.right, num))

        def dfs(rt):
            if not rt:
                return False
            
            val = k - rt.val
            return (val * 2 != k and bst(root, val)) or dfs(rt.left) or dfs(rt.right)
        return dfs(root)
            
            
