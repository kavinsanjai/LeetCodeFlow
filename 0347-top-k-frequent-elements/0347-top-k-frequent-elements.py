class Solution(object):
    def topKFrequent(self, nums, k):
        if len(nums)==1:
            return nums
        frequency=Counter(nums).most_common()
        new=[]
        count=0
        print(frequency)
        for i, j in frequency:
            new.append(i)
            count+=1
            if count>=k:
                break

        return new

            