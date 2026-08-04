# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        items = []
        self.dfs(root, items)
        items.sort()
        items = list(set(items))
        return items[k-1]

    def dfs(self, root, items):
        if not root:
            return
        
        items.append(root.val)
        self.dfs(root.left, items)
        self.dfs(root.right, items)