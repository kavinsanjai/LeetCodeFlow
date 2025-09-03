class Solution(object):
    def getSneakyNumbers(self, nums):
        counts=Counter(nums)
        result=[]
        for i , j in counts.items():
            if j==2:
                result.append(i)
            if len(result)==2:
                return result
                