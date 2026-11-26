class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(row, col):
            if not (0 <= row < rows and 0 <= col < cols): return
            if grid[row][col] != "1" or (row, col) in visited: return
            visited.add((row,col))
            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                dfs(row + dr, col + dc)



        visited = set()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(row, col)
                    islands += 1
        return islands


    
