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

        ans = False
        def dfs(rt):
            nonlocal ans
            if not rt:
                return
            
            val = k - rt.val
            if val * 2 != k:
                if bst(root, val):
                    ans = True
                    return
            dfs(rt.left)
            dfs(rt.right)
            return 
        dfs(root)
        return ans
            
            
