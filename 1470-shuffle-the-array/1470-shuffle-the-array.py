class Solution(object):
    def shuffle(self, nums, n):
        l=0
        r=n
        new=[]
        while(r<len(nums)):
            new.append(nums[l])
            new.append(nums[r])
            l+=1
            r+=1
        return new


        
        