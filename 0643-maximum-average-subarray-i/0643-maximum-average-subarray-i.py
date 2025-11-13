class Solution(object):
    def findMaxAverage(self, nums, k):
        mw=sum(nums[:k])
        maxi=mw
        for i in range(k,len(nums)):
            mw=mw-nums[i-k]+nums[i]
            maxi=max(maxi,mw)
        return float(maxi)/k

                

