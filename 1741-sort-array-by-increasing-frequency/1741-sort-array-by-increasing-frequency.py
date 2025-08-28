class Solution(object):
    def frequencySort(self, nums):
        count=Counter(nums)
        nums=sorted(nums,key=lambda x: (count[x], -x))
        return nums