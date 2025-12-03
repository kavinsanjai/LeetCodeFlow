class Solution(object):
    def pacificAtlantic(self, heights):
        visitedP=set()
        visitedA=set()
        rows=len(heights)
        cols=len(heights[0])
        dirs=((0,1),(1,0),(0,-1),(-1,0))
        def dfs(i,j,visited):
            visited.add((i,j))
            for ni,nj in dirs:
                di,dj=i+ni,j+nj
                if 0<=di<len(heights) and 0<=dj<len(heights[0]) and (di,dj) not in visited and heights[i][j]<=  heights[di][dj] :
                    visited.add((di,dj,))
                    dfs(di,dj,visited)        
       
        for j in range(cols):            # top row (0, j)
            if (0, j) not in visitedP:
                dfs(0, j, visitedP)
        for i in range(rows):            # left column (i, 0)
            if (i, 0) not in visitedP:
                dfs(i, 0, visitedP)
        
        for j in range(cols):            # bottom row (rows-1, j)
            if (rows - 1, j) not in visitedA:
                dfs(rows - 1, j, visitedA)
        for i in range(rows):            # right column (i, cols-1)
            if (i, cols - 1) not in visitedA:
                dfs(i, cols - 1, visitedA)
        
        both=visitedA&visitedP
        return [ [i,j] for (i,j) in both ]


        

        

        
            