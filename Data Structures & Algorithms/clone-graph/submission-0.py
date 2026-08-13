class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cloned = {}

        def dfs(node):
            if node in cloned:
                return cloned[node]

            copy = Node(node.val)
            cloned[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)