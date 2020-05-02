# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def helper(root: TreeNode) -> int:
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            self.length = max(self.length, left+right+1)
            return max(left, right) + 1
        
        self.length = 0
        helper(root)
        return self.length - 1