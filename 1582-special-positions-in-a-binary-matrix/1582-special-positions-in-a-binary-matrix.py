class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        row=[0]*len(mat)
        col=[0]*len(mat[0])
        count=0
        for i in range(0,len(mat)):
            for j in range(0,len(mat[0])):
                if mat[i][j]==1:
                    row[i]+=1
                    col[j]+=1
        
        for i in range(0,len(row)):
            for j in range(0,len(col)):
                if row[i]==1 and col[j]==1 and mat[i][j]==1:
                    count+=1
        return count
        
    