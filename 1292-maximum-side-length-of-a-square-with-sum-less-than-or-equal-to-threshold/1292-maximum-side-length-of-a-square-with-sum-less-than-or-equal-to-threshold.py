class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        # prefix = [[0] * len(mat[0]) for _ in range(len(mat))]
        # for i in range(0,len(mat)):
        #     prefix[i][0]=mat[i][0]
        #     for j in range(1,len(mat[i])):
        #         prefix[i][j]=prefix[i][j-1]+mat[i][j]
        # print(prefix)
        # row=len(mat)
        # col=len(mat[0])
        # curr=2
        # curr_sum=0
        # for i in range(len(mat)):
        #     for j in range(len(mat[i])-curr+1):
        #         if j==0:
        #             curr_sum = prefix[i][j+curr-1]
        #         else:
        #             curr_sum = prefix[i][j + curr - 1] - prefix[i][j - 1]
        #         print(curr_sum)
        row, col = len(mat), len(mat[0])

        # 2D prefix sum
        prefix = [[0]*(col+1) for _ in range(row+1)]
        for i in range(1, row+1):
            for j in range(1, col+1):
                prefix[i][j] = (
                    mat[i-1][j-1]
                    + prefix[i-1][j]
                    + prefix[i][j-1]
                    - prefix[i-1][j-1]
                )

        max_side = 0

        # Try all possible square sizes
        for k in range(1, min(row, col) + 1):
            found = False
            for i in range(k, row+1):
                for j in range(k, col+1):
                    square_sum = (
                        prefix[i][j]
                        - prefix[i-k][j]
                        - prefix[i][j-k]
                        + prefix[i-k][j-k]
                    )
                    if square_sum <= threshold:
                        max_side = k
                        found = True
            if not found:
                break

        return max_side



        
                
            