class Solution(object):
    def orangesRotting(self, grid):
        visited=set()
        dirs=((1,0),(0,1),(-1,0),(0,-1))
        q=deque()
        mini=0
        fresh=0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        
        if fresh==0:
            return 0
      
        while q and fresh>0:
            for _ in range(len(q)):
                i,j=q.popleft()
                for di,dj in dirs:
                    ni=di+i
                    nj=dj+j
                    if 0<=ni<len(grid) and 0<=nj<len(grid[0])  and grid[ni][nj]==1:
                        q.append((ni,nj))
                        fresh-=1
                        grid[ni][nj]=2
            mini+=1
        
        if fresh>0:
            return -1
        else:
            return mini
        
        
                