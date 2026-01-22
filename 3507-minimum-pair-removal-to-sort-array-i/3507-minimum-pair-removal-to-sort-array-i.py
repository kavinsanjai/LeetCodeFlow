class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def findminsum(nums):
            mini=float('inf')
            ci,cj=0,0
            for i in range(0,len(nums)-1):
                if nums[i]+nums[i+1]<mini:
                     ci,cj=i,i+1
                     mini=nums[i]+nums[i+1]   
            nums[ci]=nums[ci]+nums[cj]
            nums.pop(cj)
            return nums
        
        def greater(nums):
            for i in range(1,len(nums)):
                if nums[i]<nums[i-1]:
                    return True
            else:
                return False
        
        n=len(nums)
        count=0
        while greater(nums):
            nums=findminsum(nums)
            count+=1
        return count
        
        