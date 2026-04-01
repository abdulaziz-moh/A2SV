# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        status = False
        def bst(root, num):
            nonlocal status
            if not root:
                return
            val = root.val
            if num == val:
                status = True
                return
            elif num < val:
                bst(root.left, num)
            else:
                bst(root.right, num)
            return

        ans = False
        def dfs(rt):
            nonlocal ans, status
            if not rt:
                return
            
            val = k - rt.val
            if val * 2 != k:
                status = False
                bst(root, val)
                if status:
                    ans = True
                    return
            dfs(rt.left)
            dfs(rt.right)
            return 
        dfs(root)
        return ans
            
            
