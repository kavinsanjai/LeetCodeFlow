class Solution(object):
    def specialArray(self, nums):
        j=0
        for i in range(0,len(nums)+1):
            count=0
            j=0
            while(j!=len(nums)):
                if nums[j]>=i:
                    count=count+1
                j+=1
            if (count==i):
                return i
        return -1