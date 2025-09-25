class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        new=[]
        for i in range(0,rows):
            for j in range(0,cols):
                new.append([i,j])
        new.sort(key=lambda x:(abs(rCenter-x[0])+abs(cCenter-x[1])))
        return new

        