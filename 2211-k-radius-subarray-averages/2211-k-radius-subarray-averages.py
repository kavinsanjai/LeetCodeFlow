class Solution(object):
    def getAverages(self, nums, k):
        result=[-1]*len(nums)
        if len(nums)<2*k+1:
            return result
        winsum=sum(nums[:2*k+1])
        result[k]=winsum//(2*k+1)
       
        i=2*k+1
        while(i<len(nums)):
            winsum=winsum-nums[i-2*k-1]+nums[i]
            result[i-k]=winsum//(2*k+1)
            i+=1
        return result


        