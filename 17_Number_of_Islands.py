class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid: List[List[str]], i: int, j: int):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[i]) or grid[i][j] == '0':
                return 0
            grid[i][j] = '0'
            dfs(grid, i-1, j)
            dfs(grid, i+1, j)
            dfs(grid, i, j-1)
            dfs(grid, i, j+1)
            return 1
    
        final = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    final += dfs(grid, i, j)
        return final