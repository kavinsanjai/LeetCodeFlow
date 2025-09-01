class Solution(object):
    def rotate(self, nums, k):
        k=k%len(nums)
        n=len(nums)-k
        nums[:]= nums[n:]+nums[:n]
        