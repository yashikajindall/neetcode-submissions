# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.best = 0

        def depth(root):
            if root is None:
                return 0

            leftDepth = depth(root.left)
            rightDepth = depth(root.right)
            self.best = max(leftDepth + rightDepth, self.best)
            return 1 + max(leftDepth, rightDepth)

        depth(root)
        return self.best
        
        
        