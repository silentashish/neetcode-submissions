class UnionFind:

  def __init__(self, grid):
    self.parent = {}
    self.rank = {}
    self.count = 0

    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
      for c in range(cols):
        if grid[r][c] == '1':
          node_id = r * cols + c
          self.parent[node_id] = node_id
          self.rank[node_id] = 0
          self.count += 1

  def find(self, i):
    # Path compression
    if self.parent[i] != i:
      self.parent[i] = self.find(self.parent[i])
    return self.parent[i]

  def union(self, x, y):
    root_x = self.find(x)
    root_y = self.find(y)

    # If they are already in the same set, do nothing
    if root_x != root_y:
      # Union by rank
      if self.rank[root_x] > self.rank[root_y]:
        self.parent[root_y] = root_x
      elif self.rank[root_x] < self.rank[root_y]:
        self.parent[root_x] = root_y
      else:
        self.parent[root_y] = root_x
        self.rank[root_x] += 1

      # Merging two sets decreases total islands by 1
      self.count -= 1


class Solution:

  def numIslands(self, grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
      return 0

    rows, cols = len(grid), len(grid[0])
    dsu = UnionFind(grid)

    for r in range(rows):
      for c in range(cols):
        if grid[r][c] == '1':
          current_id = r * cols + c

          # Check down
          if r + 1 < rows and grid[r + 1][c] == '1':
            down_id = (r + 1) * cols + c
            dsu.union(current_id, down_id)

          # Check right
          if c + 1 < cols and grid[r][c + 1] == '1':
            right_id = (r * cols) + (c + 1)
            dsu.union(current_id, right_id)

    return dsu.count