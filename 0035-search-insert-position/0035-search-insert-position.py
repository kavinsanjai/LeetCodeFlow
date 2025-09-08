class Solution(object):
    def searchInsert(self, nums, target):
        value=0
        n=len(nums)
        for i in range(0,n):
            if(target==nums[i]):
                return i
            if(nums[n-1]<target):
                return n
            else:
                if(i==0):
                    if(nums[i]>target):
                        return i
                else:
                    if(value<target and target<nums[i]):
                        return i
                value=nums[i]
                
            
            
            

            
                
            
              