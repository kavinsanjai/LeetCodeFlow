class Solution(object):
    def maximumWealth(self, accounts):
        maxi=float('-inf')
        for i in range(0,len(accounts)):
            sub_sum=sum(accounts[i])
            if sub_sum>maxi:
                maxi=sub_sum
        return maxi