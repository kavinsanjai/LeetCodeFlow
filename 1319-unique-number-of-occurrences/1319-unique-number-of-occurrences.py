class Solution(object):
    def uniqueOccurrences(self, arr):
        frequency=Counter(arr)
        new=[]
        for i ,j  in frequency.items():
            if j in new:
                return False
            else:
                new.append(j)
        return True