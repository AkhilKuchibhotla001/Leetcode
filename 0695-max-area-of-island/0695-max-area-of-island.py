class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area_of_island = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    max_area_of_island = max(max_area_of_island , self.dfs(grid , r , c))
        return  max_area_of_island

    def dfs(self , grid , r , c):

        if (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != 1):
            return 0

        grid[r][c] = 0

        area = 1

        area += self.dfs(grid , r + 1, c)
        area += self.dfs(grid , r - 1, c)
        area += self.dfs(grid , r , c + 1)
        area += self.dfs(grid , r , c - 1)

        return area




                    
        