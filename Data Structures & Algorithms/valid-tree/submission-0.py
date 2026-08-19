from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dir_map = defaultdict(list)

        for f, t in edges:
            dir_map[f].append(t)
            dir_map[t].append(f)
        
        
        visited = set()
        
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)

            for n in dir_map[node]:
                if n == parent:
                    continue
                
                if not dfs(n, node):
                    return False

            return True
        
        if not dfs(0, -1):
            return False
                
        return len(visited) == n
        