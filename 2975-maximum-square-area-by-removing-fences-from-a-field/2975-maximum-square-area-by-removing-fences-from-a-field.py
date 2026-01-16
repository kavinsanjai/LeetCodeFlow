class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        # if m == n :
        #     m-=1
        #     return m*m

        # hFences.append(m)
        # vFences.append(n)

        # while hFences and vFences:
        #     htop=hFences[-1]
        #     vtop=vFences[-1]
        #     print(htop,vtop)

        #     if htop == vtop:
        #         htop-=1
        #         vtop-=1
        #         return htop*htop
            
        #     elif htop > vtop:
        #         hFences.pop()
            
        #     else:
        #         vFences.pop()
        
        # return -1
        if m == n:
            return (m-1)*(m-1)

        hFences=[1]+sorted(hFences)+[m]
        vFences=[1]+sorted(vFences)+[n]

        gaps=set()
        for i in range(0,len(hFences)):
            for j in range(i+1,len(hFences)):
                gaps.add(hFences[j]-hFences[i])

        max_len=float('-inf')
        for i in range(0,len(vFences)):
            for j in range(i+1,len(vFences)):
                if vFences[j]-vFences[i] in gaps:
                    max_len=max(max_len,vFences[j]-vFences[i])
        

        if max_len>0:
            return (max_len*max_len)%(10**9+7)
        else:
            return -1