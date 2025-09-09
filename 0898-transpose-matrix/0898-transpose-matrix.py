class Solution(object):
    def transpose(self, matrix):
        rows,cols=len(matrix),len(matrix[0])
        new_matrix=[[0]*rows for _ in range(cols)]
        
        
        for i in range(0,rows):
            for j in range(0,cols):
                new_matrix[j][i]=matrix[i][j]
        return new_matrix
        