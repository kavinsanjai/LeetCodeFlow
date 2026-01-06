class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """

        if m * k > len(bloomDay):
            return -1
        def isPossible(days):
            bou=0
            flo=0
            for d in bloomDay:
                if d <= days:
                    flo += 1
                    if flo == k:
                        bou += 1
                        flo = 0
                else:
                    flo = 0
            return bou>=m

        mini=min(bloomDay)
        maxi=max(bloomDay)
        while(mini<maxi):
            mid=mini+(maxi-mini)//2
            if isPossible(mid):
                maxi=mid
            else:
                mini=mid+1
        return mini

        