# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        def dfs(root: TreeNode, arr: List[int], depth: int):
            if not root:
                return False
            if depth >= len(arr) or root.val != arr[depth]:
                return False
            if not root.left and not root.right:
                return depth == len(arr) - 1
            return dfs(root.left, arr, depth+1) or dfs(root.right, arr, depth+1)
        
        return dfs(root, arr, 0)