class Solution(object):
    def trap(self, height):
        maxleft = [0]*len(height)
        maxright = [0]*len(height)

        maxleft[0] = height[0]
        for i in range(1, len(height)):
            maxleft[i] = max(height[i], maxleft[i-1])

        maxright[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2, -1, -1):
            maxright[i] = max(height[i], maxright[i+1])
        total_water=0
        for i in range(0,len(height)):
            total_water+=min(maxright[i],maxleft[i])-height[i]
        return total_water
        
        