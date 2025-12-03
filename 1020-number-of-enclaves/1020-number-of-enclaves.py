class Solution(object):
    def numEnclaves(self, grid):
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        count=0
        dirs=((1,0),(0,1),(-1,0),(0,-1))
        def dfs(i,j):
            grid[i][j]=0
            for di,dj in dirs:
                ni,nj=i+di,j+dj
                if 0<=ni<rows and 0<=nj<cols and  grid[ni][nj]==1:
                    dfs(ni,nj)

        for j in range(0,cols):
            if grid[0][j]==1:
                dfs(0,j)
        for i in range(0,rows):
            if grid[i][0]==1:
                dfs(i,0)
        
        for j in range(0,cols):
            if grid[rows-1][j]==1:
                dfs(rows-1,j)
        for i in range(0,rows):
            if grid[i][cols-1]==1:
                dfs(i,cols-1)
        

        for i in range(0,rows):
            for j in range(0,cols):
                if grid[i][j]==1:
                    count+=1
        return count

        
        