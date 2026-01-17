class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        area=0
        for i in range(0,len(bottomLeft)):
            for j in range(i+1,len(topRight)):
                minx=max(bottomLeft[i][0],bottomLeft[j][0])
                miny=max(bottomLeft[i][1],bottomLeft[j][1])
                maxx=min(topRight[i][0],topRight[j][0])
                maxy=min(topRight[i][1],topRight[j][1])

                if minx<maxx and miny<maxy:
                    side=min(maxx-minx,maxy-miny)
                    area= max(side*side,area)
        
        return area

