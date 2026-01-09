class Solution(object):
    def kthLargestNumber(self, nums, k):
        for i in range(0,len(nums)):
            nums[i]=int(nums[i])

        nums.sort()
        return str(nums[-k])   