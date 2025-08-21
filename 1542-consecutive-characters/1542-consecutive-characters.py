class Solution(object):
    def maxPower(self, s):
        if len(s)==1:
            return 1
        count=1
        maxi=0
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count=count+1
            else:
                count=1
            maxi = max(maxi, count)
        return maxi
        