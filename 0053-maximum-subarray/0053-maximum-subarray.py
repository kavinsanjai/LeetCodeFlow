class Solution(object):
    def maxSubArray(self, nums):
        n=len(nums)
        curr=0
        max_c=nums[0]
        for i in range(0,n):
            if curr<0:
                curr=0            
            curr+=nums[i]
            max_c=max(curr,max_c)
        return max_c

                