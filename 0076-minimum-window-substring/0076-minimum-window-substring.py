class Solution(object):
    def satisfied(self,s,t):
        for key in t:
            if s.get(key, 0) < t[key]:
                return False
        return True
    def minWindow(self, s, t):
        fre_t=Counter(t)
        print(fre_t)
        fre_w={}
        l=0
        left,right=0,0
        min_len=float('inf')
        for i in range(0,len(s)):
            fre_w[s[i]]=fre_w.get(s[i],0)+1
            while(self.satisfied(fre_w,fre_t)):
                if min_len > i-l+1:
                    left=l
                    right=i+1
                    min_len=i-l+1
                if fre_w[s[l]] > 1:
                    fre_w[s[l]] -= 1
                else:
                    del fre_w[s[l]]
                l+=1
        return s[left:right]

            
