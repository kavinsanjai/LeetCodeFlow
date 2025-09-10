class Solution(object):
    def maxProduct(self, nums):
        max_pro=nums[0]
        curr_pro=nums[0]
        curr_prom=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0:
                curr_pro,curr_prom=curr_prom,curr_pro

            curr_pro=max(nums[i],curr_pro*nums[i])
            curr_prom=min(nums[i],curr_prom*nums[i])
            max_pro=max(max_pro,curr_pro)
        return max_pro
        