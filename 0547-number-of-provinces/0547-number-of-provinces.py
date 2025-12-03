class Solution(object):
    def findCircleNum(self, isConnected):
        q=deque()
        visited=set()
        dirs=((1,0),(0,1),(-1,0),(0,-1))
        count=0
        def dfs(i):
            visited.add(i)
            for new in range(0,len(isConnected[0])): 
                if isConnected[i][new]==1 and new not in visited:
                    visited.add(new)
                    dfs(new)    
        
        
        for i in range(0,len(isConnected)):
            if i not in visited:
                count+=1
                dfs(i)
        return count


            
            
        