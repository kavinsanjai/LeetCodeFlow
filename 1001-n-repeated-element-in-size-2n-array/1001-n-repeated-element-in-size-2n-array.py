class Solution(object):
    def repeatedNTimes(self, nums):
        frequency=Counter(nums)
        return frequency.most_common(1)[0][0]    
        