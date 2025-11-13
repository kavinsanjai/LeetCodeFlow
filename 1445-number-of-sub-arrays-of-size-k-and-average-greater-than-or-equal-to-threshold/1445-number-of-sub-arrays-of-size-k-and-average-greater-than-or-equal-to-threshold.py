class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        if len(arr)<k:
            return 0
        count=0
        win_size=sum(arr[:k])
        if (win_size)/k>=threshold:
            count+=1
        for i in range(k,len(arr)):
            win_size+=arr[i]-arr[i-k]
            if (win_size)/k>=threshold:
                count+=1
        return count
        