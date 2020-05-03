class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        h = len(matrix)
        w = len(matrix[0])
        answer = 0
        dp = [[0 for i in range(w)] for i in range(h)]
        
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == '1':
                    dp[i][j] = 1
                    if i>0 and j>0:
                        dp[i][j] += min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                answer = max(answer, dp[i][j])
        
        return answer**2