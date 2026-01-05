class Solution(object):
    def maxMatrixSum(self, matrix):
        neg_count=0
        total_val=0
        min_abs=float('inf')
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                    if matrix[i][j]<0:
                        neg_count+=1
                    total_val+=abs(matrix[i][j])
                    min_abs=min(min_abs,abs(matrix[i][j]))
        if neg_count%2==0:
            return total_val
        else:
            return total_val-2*min_abs

        