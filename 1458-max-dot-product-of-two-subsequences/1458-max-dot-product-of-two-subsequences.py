class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        dp=[[float('-inf') for i in range(0,len(nums2)+1)] for j in range(0,len(nums1)+1)]
        for i in range(0,len(nums1)):
            for j in range(0,len(nums2)):
                curr=nums1[i]*nums2[j]
                dp[i+1][j+1]=max(curr+dp[i][j],dp[i][j+1],dp[i+1][j],curr) 
        return dp[len(nums1)][len(nums2)]