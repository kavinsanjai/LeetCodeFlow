class Solution(object):
    def findMaxAverage(self, nums, k):
        curr_sum=sum(nums[0:k])
        maxi=curr_sum
        for i in range(k,len(nums)):
            curr_sum+=nums[i]-nums[i-k]
            if curr_sum>maxi:
                maxi=curr_sum
        return maxi/float(k)            
        