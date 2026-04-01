# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)

        ans = 0
        while queue:
            x = queue.popleft()

            if x.val % 2 == 0:
                a = x.left
                b = x.right
                if a != None:
                    ans += (a.left.val if a.left else 0)
                    ans += (a.right.val if a.right else 0)
                if b != None:
                    ans += (b.left.val if b.left else 0)
                    ans += (b.right.val if b.right else 0)
            
            if x.left:
                queue.append(x.left)
            if x.right:
                queue.append(x.right)
        return ans


