class Solution(object):
    def findPeakElement(self, nums):
        index=0
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                index=i
        return index