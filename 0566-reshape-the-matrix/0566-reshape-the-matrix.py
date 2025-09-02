class Solution(object):
    def matrixReshape(self, mat, r, c):
        rows,cols=len(mat),len(mat[0])
        if rows*cols != r * c:
            return mat
        sub=[]
        main=[]
        for i in range(0,len(mat)):
            for j in range(0,len(mat[i])):
                sub.append(mat[i][j])
                if len(sub)==c:
                    main.append(sub)
                    sub=[]
        return main


                