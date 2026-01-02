class Solution(object):
    def repeatedNTimes(self, nums):
        fre=[]
        for i in range(0,len(nums)):
            if nums[i] in fre:
                return nums[i]
            else:
                fre.append(nums[i])
        
        