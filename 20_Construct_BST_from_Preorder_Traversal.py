# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode: 
        if not preorder:
            return None
        root_val = preorder[0]
        lower = []
        higher = []
        bst = TreeNode(root_val)
        for i in range(1, len(preorder)):
            if preorder[i] < root_val:
                lower.append(preorder[i])
            else:
                higher.append(preorder[i])
        bst.left = self.bstFromPreorder(lower)
        bst.right = self.bstFromPreorder(higher)
        return bst