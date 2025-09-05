class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero=[]
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if matrix[i][j]==0:
                    zero.append([i,j])
        print(zero)
        for row,cols in zero:
            matrix[row]=[0]*len(matrix[0])
            for j in range(0,len(matrix)):
                matrix[j][cols]=0


        