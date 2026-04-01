# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def dfs(root, sm, temp, ans):
            if not root:
                return []
            sm += root.val
            temp.append(root.val)

            if not root.left and not root.right:
                if sm == targetSum:
                    ans.append(temp[:])
                    return ans
            dfs(root.left, sm, temp[:], ans)
            dfs(root.right, sm, temp[:], ans)

            return ans
        
        return dfs(root, 0, [], [])