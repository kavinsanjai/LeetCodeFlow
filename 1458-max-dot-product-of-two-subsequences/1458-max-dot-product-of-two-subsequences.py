class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        m=len(nums1)
        n=len(nums2)
        dp=[[float('-inf') for i in range(0,n+1)] for j in range(0,m+1)]
        for i in range(0,m):
            for j in range(0,n):
                curr=nums1[i]*nums2[j]
                dp[i+1][j+1]=max(curr+dp[i][j],dp[i][j+1],dp[i+1][j],curr) 
        return dp[m][n]