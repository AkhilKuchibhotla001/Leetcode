class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        queue = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r , c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        
        while queue and fresh > 0:
            for _ in range(len(queue)):

                r , c  = queue.popleft()

                directions = [( 1 , 0) , (-1 , 0) , (0 , 1) , (0 , -1)]

                for dr , dc in directions:

                    nr = r + dr 
                    nc = c + dc

                    if (nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] != 1):

                        continue

                    grid[nr][nc] = 2

                    fresh -= 1

                    queue.append((nr , nc))

            minutes += 1
        if fresh == 0:
            return minutes
        else:
            return -1



        
        