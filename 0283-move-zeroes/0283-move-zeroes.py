class Solution(object):
    def moveZeroes(self, nums): 
        nums[:]=sorted(nums,key=lambda x:(x==0))
