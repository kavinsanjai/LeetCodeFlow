class Solution(object):
    def maxSubArray(self, nums):
        maxi=nums[0]
        curr_sum=nums[0]
        for i in range(1,len(nums)):
            curr_sum=max(nums[i],curr_sum+nums[i])
            maxi=max(curr_sum,maxi)
        return maxi

                