class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(i, j, visited, prev_height):
            if (i < 0 or i >= ROWS or j < 0 or j >= COLS
                    or (i, j) in visited
                    or heights[i][j] < prev_height):
                return
            visited.add((i, j))
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                dfs(i + di, j + dj, visited, heights[i][j])

        for j in range(COLS):
            dfs(0, j, pacific, heights[0][j])
            dfs(ROWS - 1, j, atlantic, heights[ROWS - 1][j])

        for i in range(ROWS):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, COLS - 1, atlantic, heights[i][COLS - 1])

        return [[i, j] for i, j in pacific & atlantic]