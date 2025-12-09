class Solution(object):
    def maxProfit(self, prices):
        mini=prices[0]
        maxi=0
        for i in range(0,len(prices)):
            mini=min(mini,prices[i])
            maxi=max(prices[i]-mini,maxi)
        return maxi

        