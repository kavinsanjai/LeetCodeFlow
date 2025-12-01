class Solution(object):
    def numIslands(self, grid):

        visited=set()
        q=deque()
        count=0
        dire=((1,0),(0,1),(-1,0),(0,-1))
        for rowi in range(0,len(grid)):
            for colj in range(0,len(grid[0])):
                if grid[rowi][colj]=='1' and (rowi,colj)not in visited:
                    q.append((rowi,colj))
                    visited.add((rowi,colj))
                    count+=1
                    while q:
                        i,j=q.popleft() 
        
                        for di,dj in dire:
                            ni=di+i
                            nj=dj+j
                            if (0<=ni<len(grid)) and (0<=nj<len(grid[0])) and (ni,nj)not in visited and grid[ni][nj]=='1':
                                q.append((ni,nj))
                                visited.add((ni,nj))
        return count
                                            
                        
