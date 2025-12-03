class Solution(object):
    def numEnclaves(self, grid):
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        count=0
        dirs=((1,0),(0,1),(-1,0),(0,-1))
        def dfs(i,j):
            visited.add((i,j))
            grid[i][j]=0
            for di,dj in dirs:
                ni,nj=i+di,j+dj
                if 0<=ni<rows and 0<=nj<cols and (ni,nj) not in visited and grid[ni][nj]==1:
                    dfs(ni,nj)

        for j in range(0,cols):
            if (0,j) not in visited and grid[0][j]==1:
                dfs(0,j)
        for i in range(0,rows):
            if(i,0) not in visited and grid[i][0]==1:
                dfs(i,0)
        
        for j in range(0,cols):
            if(rows-1,j) not in visited and grid[rows-1][j]==1:
                dfs(rows-1,j)
        for i in range(0,rows):
            if(i,cols-1) not in visited and grid[i][cols-1]==1:
                dfs(i,cols-1)
        

        for i in range(0,rows):
            for j in range(0,cols):
                if grid[i][j]==1:
                    count+=1
        return count

        
        