class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        l=0
        count=0
        curr_sum=0
        zeros=0
        for i in range(0,len(nums)):
            curr_sum+=nums[i]
            
            while(l<i and (curr_sum>goal or nums[l]==0)):
                    if nums[l]==0:
                        zeros+=1
                    else:
                        zeros=0
                    curr_sum-=nums[l]
                    l+=1
            if curr_sum==goal:
                count+=1+zeros
        
        return count
                

        