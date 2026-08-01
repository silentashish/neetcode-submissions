# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.treeExplore(root,0)
        
    # create a new function
    def treeExplore(self, root, length):
    # recursion on both right and left
        if not root:
            return length
        else:
            return max(self.treeExplore(root.left, length + 1), self.treeExplore(root.right, length + 1) )
