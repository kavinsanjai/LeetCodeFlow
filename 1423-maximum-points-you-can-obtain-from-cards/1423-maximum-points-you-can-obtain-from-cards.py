class Solution(object):
    def maxScore(self, cardPoints, k):
        sum1=sum(cardPoints[:k])
        curr_sum=sum1
        max_sum=curr_sum
        l,r=k-1,len(cardPoints)-1
        for i in range(0,k):
                curr_sum-=cardPoints[l]
                curr_sum+=cardPoints[r]
                max_sum=max(max_sum,curr_sum)
                l-=1
                r-=1
        return max_sum
            
            