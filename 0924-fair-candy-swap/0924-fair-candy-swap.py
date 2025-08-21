class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        sumA, sumB = sum(aliceSizes), sum(bobSizes)
        diff = (sumA - sumB) // 2   

        setB = set(bobSizes)        
        for a in aliceSizes:
            b = a - diff
            if b in setB:
                return [a, b]
            

                
        