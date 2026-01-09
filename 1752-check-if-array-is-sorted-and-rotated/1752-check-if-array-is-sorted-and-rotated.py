class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dup=nums[:]
        dup.sort()
        if nums==dup:
            return True

        for i in range(0,len(nums)):
            if nums[i:]+nums[:i]==dup:
                return True
        else:
            return False


        