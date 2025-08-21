class Solution(object):
    def countPairs(self, nums, target):
        nums.sort()
        count=0
        sums=0
        for i in range(0,len(nums)):
            j=i+1
            while(j<len(nums)):
                sums=nums[i]+nums[j]
                if(sums<target):
                    count=count+1
                j+=1
                
        return count

        