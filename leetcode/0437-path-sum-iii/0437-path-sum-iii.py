# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        if not root:
            return 0
        
        def dfs(root, sm):
            if not root:
                return 0
            sm += root.val
            count = (1 if sm == targetSum else 0)

            count += dfs(root.left, sm)
            count += dfs(root.right, sm)
            
            return count
        return (
            dfs(root, 0)
            + self.pathSum(root.left, targetSum)
            + self.pathSum(root.right, targetSum)
        )