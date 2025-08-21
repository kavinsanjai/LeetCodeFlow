class Solution(object):
    def balancedStringSplit(self, s):
        count=0
        balance=0
        for i in range(0,len(s)):
            if s[i]=='R':
                balance+=1
            if s[i]=='L':
                balance-=1
            if balance==0:
                count+=1
        return count
                
