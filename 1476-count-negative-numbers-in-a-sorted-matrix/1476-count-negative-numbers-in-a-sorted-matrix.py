class Solution(object):
    def countNegatives(self, grid):
        count=0
        for i in range(0,len(grid)):
            grid[i].sort()
            for j in range(0,len(grid[i])):
                if grid[i][j]<0:
                    count+=1
                else:
                    break
        return count
                