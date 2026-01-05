class Solution(object):
    def containsDuplicate(self, nums):
        # dic={}
        # count=0
        # for i in range(0,len(nums)):
        #     if nums[i] not in dic:
        #         dic[nums[i]]=count+1
        #     else:
        #         return True
        # return False
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False