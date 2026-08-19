from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = defaultdict(list)   
        
        for c, p in prerequisites:
            course_map[c].append(p)
        
        visiting = set()

        def dfs(c):
            if c in visiting:
                return False
            if course_map[c] == []:
                return True

            visiting.add(c)
            
            for pre in course_map[c]:
                if not dfs(pre):
                    return False

            visiting.remove(c)
            course_map[c] = []
            return True

        

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
