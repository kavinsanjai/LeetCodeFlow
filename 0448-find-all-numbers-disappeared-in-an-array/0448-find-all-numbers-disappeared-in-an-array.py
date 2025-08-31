class Solution(object):
    def findDisappearedNumbers(self, nums):
        n=len(nums)
        full_set = set(range(1, n+1))
        nums_set=set(nums)
        missing=list(full_set-nums_set)
        return missing