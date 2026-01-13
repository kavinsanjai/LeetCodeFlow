class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def findarea(value):
            return value*value
        
        square_value=[0]*len(squares)

        start=float('inf')
        end=float('-inf')
        for i in range(0,len(squares)):
            square_value[i]=findarea(squares[i][2])
            if start>squares[i][1]:
                start=squares[i][1]
            if end<squares[i][1]+squares[i][2]:
                end=squares[i][1]+squares[i][2]


        def findifcorrect(mid):
            firsthalf=0
            secondhalf=0
            
            for i in range(0,len(squares)):
                if squares[i][1]+squares[i][2]<=mid:
                    firsthalf+=square_value[i]

                elif squares[i][1]>=mid:
                    secondhalf+=square_value[i]
                
                else:
                    top=squares[i][1]+squares[i][2]
                    below_h=mid-squares[i][1]
                    firsthalf+=below_h*squares[i][2]
                    above_h=top-mid
                    secondhalf+=above_h*squares[i][2]
            return firsthalf>=secondhalf

        
        while end-start>1e-6:
            mid=(start+end)/2
            if findifcorrect(mid):
                end=mid
            else:
                start=mid
        return start
