class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        taken=0
        indegree = {i: 0 for i in range(numCourses)}      
        for course, prereq in prerequisites:
            indegree[course] += 1    
        q=deque()
        
        for i,j in indegree.items():
            if j==0:
                q.append(i)


        while q:
            node=q.popleft()
            taken+=1    
            for i,j in prerequisites:
                if node==j:
                    indegree[i]-=1
                    if indegree[i]==0:
                        q.append(i)
            
        
        if taken==numCourses:
            return True
        else:
            return False
        
        