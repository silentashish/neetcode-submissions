# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        level = 0
        self.dfs(root, result, level)
        return result

    
    def dfs(self, root, result, level):
        if not root:
            return None
        
        if len(result) == level:
            result.append([])
        
        result[level].append(root.val)

        self.dfs(root.left, result, level + 1)
        self.dfs(root.right, result, level + 1)
        





        