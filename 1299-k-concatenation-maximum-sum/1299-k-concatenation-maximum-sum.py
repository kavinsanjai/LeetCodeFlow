class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        range1=10**9+7
        def kadane(arr):
            max_sum=arr[0]
            curr_sum=arr[0]
            for i in range(1,len(arr)):
                curr_sum=max(arr[i],curr_sum+arr[i])
                if max_sum<=curr_sum:
                    max_sum=curr_sum
            return max_sum
        
        if k==1:
            return max(0,kadane(arr))%range1

        total_sum=sum(arr)
        double=kadane(arr*2)
        if total_sum>0:
            return max(0,double+(k-2)*total_sum)%range1
        else:
            return (double if double>=0 else 0) %range1
