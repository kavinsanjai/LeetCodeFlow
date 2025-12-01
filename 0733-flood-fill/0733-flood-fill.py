from collections import deque
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        ni,nj=0,0
        q=deque()
        dir=[(1,0),(0,1),(-1,0),(0,-1)]
        q.append((sr,sc))
        org=image[sr][sc]        
        visited=set()
        while q:
            i,j=q.popleft()
            if (i,j) not in visited :
                visited.add((i,j))
                image[i][j]=color
            for di , dj in dir:
                ni,nj=i+di,j+dj
                if 0<=ni<len(image) and 0<=nj<len(image[0]) and (ni,nj) not in visited:
                    if image[ni][nj]==org:
                        q.append((ni,nj))        
        return image
        