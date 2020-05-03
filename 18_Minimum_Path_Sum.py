class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        solution = [[0 for i in range(n)] for j in range(m)]
        dummy = 1e9
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    solution[i][j] = grid[i][j]
                else:
                    solution[i][j] = grid[i][j] + min(dummy if i == 0 else solution[i-1][j], dummy if j == 0 else solution[i][j-1])
                
        return solution[m-1][n-1]