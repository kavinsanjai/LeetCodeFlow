class Solution(object):
    def minEatingSpeed(self, piles, h):
        max_pile=0
        low=1
        min_hr=float('inf')
        hr=0
        max_pile=max(piles)
        while(low<=max_pile):
            hr=0
            speed=low+(max_pile-low)//2
            for i in range(0,len(piles)):
                hr+=(piles[i]+speed-1)//speed
            if hr<=h:
                max_pile=speed-1
            else:
                low=speed+1
        return  low   


            
        