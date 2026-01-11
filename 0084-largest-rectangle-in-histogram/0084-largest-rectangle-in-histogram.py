class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
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
