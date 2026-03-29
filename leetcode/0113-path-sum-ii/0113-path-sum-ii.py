# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def dfs(root, sm, temp):
            if not root:
                return
            sm += root.val
            temp.append(root.val)
            # print(temp)
            # print(sm)
            if not root.left and not root.right:
                if sm == targetSum:
                    self.ans.append(temp[:])
            dfs(root.left, sm, temp[:])
            dfs(root.right, sm, temp[:])
            return
        dfs(root, 0, [])
        return self.ans
                
