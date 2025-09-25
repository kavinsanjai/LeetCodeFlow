class Solution(object):
    def isBoomerang(self, points):
        (x1,y1),(x2,y2),(x3,y3)=points
        if (x1,y1)==(x2,y2) or (x2,y2)==(x3,y3) or (x3,y3)==(x1,y1):
            return False
        value = x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)
        return True if value!=0 else False