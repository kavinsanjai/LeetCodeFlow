class Solution(object):
    def rob(self, nums):
        def helper(nums1):
            rob1, rob2 = 0 , 0
            for n in nums1:
                temp = max(rob1+n,rob2)
                rob1=rob2
                rob2=temp
            return rob2
        n=len(nums)
        if n==1:
            return nums[0]
        return max(helper(nums[:-1]),helper(nums[1:]))

        