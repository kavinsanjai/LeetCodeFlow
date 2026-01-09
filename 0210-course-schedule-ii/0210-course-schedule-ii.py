class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        indegree = {i: 0 for i in range(numCourses)}      
        for course, prereq in prerequisites:
            indegree[course] += 1    
        q=deque()
        res=[]

        for i,j in indegree.items():
            if j==0:
                q.append(i)
        
        

        while q:
            node=q.popleft()
            res.append(node)  
            for i,j in prerequisites:
                if node==j:
                    indegree[i]-=1
                    if indegree[i]==0:
                        q.append(i)
            
        
        return res if len(res) == numCourses else []
        