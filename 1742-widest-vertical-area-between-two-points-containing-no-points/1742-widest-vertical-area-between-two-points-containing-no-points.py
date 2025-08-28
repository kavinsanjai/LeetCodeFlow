class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        maxi=0
        points.sort()
        for i in range(1,len(points)):
            sub=points[i][0]-points[i-1][0]
            if sub >maxi:
                maxi=sub
        return maxi
        