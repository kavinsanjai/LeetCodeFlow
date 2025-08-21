class Solution(object):
    def maximumCount(self, nums):
        count_negative=0
        zero=0
        for i in nums:
            if i<0:
                count_negative+=1
            elif i==0:
                zero+=1
            else:
                break
        count_positive = len(nums) - count_negative - zero
        return max(count_negative, count_positive)