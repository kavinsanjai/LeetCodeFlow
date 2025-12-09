class Solution(object):
    def minPathSum(self, grid):
        rows=len(grid)
        cols=len(grid[0])
        dp=[]
        for i in range(rows):
            dp.append([0]*(cols))
        print(dp)
        for i in range(rows):
            for j in range(cols):
                if i==0 and j==0:
                    dp[i][j]=grid[i][j]
                elif i==0:
                    dp[i][j]=grid[i][j]+dp[i][j-1]
                elif j==0:
                    dp[i][j]=grid[i][j]+dp[i-1][j]
                else:
                    dp[i][j]=grid[i][j]+min(dp[i-1][j],dp[i][j-1])
        return dp[rows-1][cols-1]

        
  
        
        