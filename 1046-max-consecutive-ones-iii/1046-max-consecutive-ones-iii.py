class Solution(object):
    def longestOnes(self, nums, k):
        max_count=0
        f_count=0
        count=0
        l=0
        for i in range(0,len(nums)):
            if nums[i]==1:
                count+=1
            else:
                f_count+=1
                count+=1
                while(f_count>k):
                    if nums[l]==0:
                        f_count-=1
                    count-=1
                    l+=1
            max_count=max(max_count,count)
        return max_count


