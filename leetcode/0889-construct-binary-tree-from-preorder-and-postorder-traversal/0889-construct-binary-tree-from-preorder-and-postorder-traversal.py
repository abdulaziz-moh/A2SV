# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        visited, n = set(), len(preorder)
        postidx = {postorder[i]: i for i in range(n)}
        preidx = {preorder[i]: i for i in range(n)}
        
        br = 0
        def rec(idx):
            nonlocal br
            if len(visited) == n or idx in visited:
                return

            val = preorder[idx]
            node = TreeNode(val)
            visited.add(idx)

            if postidx[val] <= br:
                while br < n and preidx[postorder[br]] in visited:
                    br += 1
                return node

            node.left = rec(idx + 1)
            
            rightval = postorder[postidx[val] - 1]
            a = preidx[rightval]
            
            node.right = rec(a)
            
            return node
        return rec(0)