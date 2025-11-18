class Solution(object):
    def minSubArrayLen(self, target, nums):
        l=0
        cur_sum=0
        cur_len=0
        min_len=float('inf')
        for i in range(0,len(nums)):
            cur_sum+=nums[i]
            if cur_sum >= target:
                cur_len=i-l+1
                while(cur_sum>=target):
                    cur_sum-=nums[l]
                    l+=1
                    if cur_sum >= target:
                         cur_len=i-l+1
                min_len=min(cur_len,min_len)
        return 0 if min_len > len(nums) else min_len

