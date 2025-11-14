class Solution(object):
    def checkInclusion(self, s1, s2):
        s1_f=Counter(s1)
        n=len(s1)
        w_f=Counter(s2[:n])
        if s1_f == w_f :
            return True           
        for i in range(n,len(s2)):           
          
            if w_f[s2[i-n]] == 1:
                del w_f[s2[i-n]]
            else:
                w_f[s2[i-n]]-=1
            w_f[s2[i]] = w_f.get(s2[i], 0) + 1

            if w_f == s1_f:
                return True
        return False
        