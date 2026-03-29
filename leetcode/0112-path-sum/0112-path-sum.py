from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, sm):
            if node is None:
                return False
            
            sm += node.val
            
            # base case: check if it's a leaf node
            if node.left is None and node.right is None:
                return sm == targetSum
            
            return dfs(node.left, sm) or dfs(node.right, sm)

        return dfs(root, 0)
