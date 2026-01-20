class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in range(0,len(nums)):
            for j in range(1,nums[i]):
                if j|j+1 == nums[i]:
                    ans.append(j)
                    break
            else:
                ans.append(-1)
        return ans
        