class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in range(0,len(nums)):
            if nums[i]%2==0:
                ans.append(-1)
                continue
            for j in range(31,-1,-1):
                if nums[i]&(1<<j):
                    x=nums[i]&~(1<<j)
                    if x|x+1 == nums[i]:
                        ans.append(x)
                        break
            else:
                ans.append(-1)
        return ans