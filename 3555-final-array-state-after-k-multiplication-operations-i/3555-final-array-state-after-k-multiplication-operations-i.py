class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        for i in range(0,k):
            num=min(nums)
            index=nums.index(num)
            nums[index]=nums[index]*multiplier
        return nums