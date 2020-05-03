# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(root: TreeNode):
            nonlocal maxsum
            if not root:
                return 0
            x = dfs(root.left)
            y = dfs(root.right)
            maxsum = max(maxsum, x + y + root.val)
            return max(0, root.val + max(x, y))
        
        maxsum = float('-inf')
        dfs(root)
        return maxsum