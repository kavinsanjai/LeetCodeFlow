class Solution(object):
    def getConcatenation(self, nums):
        n=len(nums)
        ans=[]
        ans[:]=nums[:]
        for i in range(0,len(nums)):
            ans.append(nums[i])
        return ans