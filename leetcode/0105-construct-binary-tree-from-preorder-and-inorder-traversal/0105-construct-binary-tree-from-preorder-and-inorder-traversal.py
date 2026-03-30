# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorderIndex = {val: i for i, val in enumerate(inorder)}
        self.preIndex = 0
        
        def build(inStart, inEnd):
            if inStart > inEnd:
                return None
            
            rootVal = preorder[self.preIndex]
            self.preIndex += 1
            
            root = TreeNode(rootVal)
            
            rootIndex = inorderIndex[rootVal]
            
            root.left = build(inStart, rootIndex - 1)
            root.right = build(rootIndex + 1, inEnd)
            
            return root
        
        return build(0, len(inorder)-1)