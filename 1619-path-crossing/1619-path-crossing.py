class Solution(object):
    def isPathCrossing(self, path):
        x=0
        y=0
        new=set()
        new.add((x,y))
        for value in path:
            if value=='N':
                x+=1
            elif value=='E':
                y+=1
            elif value=='S':
                x-=1
            else:
                y-=1
            if (x,y) in new:
                return True
            else:
                new.add((x,y))
        return False 

