class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_of_islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                  num_of_islands += 1
                  self.dfs(grid , r, c)
        return num_of_islands


    def dfs(self , grid , r, c):
        if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != "1"):
            return

        grid[r][c] = "0"
        self.dfs(grid , r + 1 , c)
        self.dfs(grid , r - 1 , c)
        self.dfs(grid , r ,c + 1)
        self.dfs(grid , r , c - 1)

    
        