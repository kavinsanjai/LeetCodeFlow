class Solution(object):
    def destCity(self, paths):
        starts=set()
        for i in range(0,len(paths)):
            starts.add(paths[i][0])
        for a,b in paths:
            if b not in starts:
                return b
       