class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        def findarea(heights):
            stack=[]
            max_area=0
            area=0
            for i in range(0,len(heights)):
                curr_ind=i
                while stack and stack[-1][1]>=heights[i]:
                    ind,value=stack.pop()
                    curr_ind=ind
                    width=i-ind
                    area=width*value
                    max_area=max(max_area,area)
                stack.append([curr_ind,heights[i]])

            while stack:
                ind,value=stack.pop()
                width=len(heights)-ind
                area=width*value
                max_area=max(max_area,area)
            return max_area

        height=[0]*len(matrix[0])
        max_area=0
        for row in matrix:
            for i in range(0,len(row)):
                if row[i]=='1':
                    height[i]+=1
                else:
                    height[i]=0
            max_area=max(max_area,findarea(height))
        return max_area