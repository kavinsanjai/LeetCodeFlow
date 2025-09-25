class Solution(object):
    def lastStoneWeight(self, stones):
        if not stones:
            return 0
        if len(stones)==1:
            return stones[0]
        
        stones.sort(reverse=True)
        max1=stones[0]
        max2=stones[1]
      
        if max1==max2:
            stones.remove(max1)
            stones.remove(max2)
            return self.lastStoneWeight(stones)
        else:
            stones[0]=max1-max2
            stones.remove(max2)
            return self.lastStoneWeight(stones)

        