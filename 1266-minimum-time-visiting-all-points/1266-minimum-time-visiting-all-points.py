class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ith,jth=points[0]
        tot=0
        for i in range(1,len(points)):
            tot+=max(abs(ith-points[i][0]),abs(jth-points[i][1]))
            ith,jth=points[i][0],points[i][1]
        return tot