class Solution(object):
    def minDistance(self, word1, word2):
        # frequency1=Counter(word1)
        # frequency2=Counter(word2)
        # count=0
        # for ch in set(frequency1.keys()) | set(frequency2.keys()):
        #     count+=abs(frequency1[ch]-frequency2[ch])
        # return count
        m=len(word1)
        n=len(word2)
        dp=[[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        LCS=dp[m][n]
        return m+n-2*LCS