class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        maxi=0
        points.sort()
        for i in range(1,len(points)):
            if (points[i][0]-points[i-1][0])>maxi:
                maxi=points[i][0]-points[i-1][0]
        return maxi
        