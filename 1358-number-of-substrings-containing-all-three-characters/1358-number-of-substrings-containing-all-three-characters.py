class Solution(object):
    def numberOfSubstrings(self, s):
        l=0
        fre=Counter()
        count=0
        
        for i in range(0,len(s)):
            fre[s[i]]=fre.get(s[i],0)+1
            while(fre['a']>0 and fre['b']>0 and fre['c']>0 ):
                count+=len(s)-i
                fre[s[l]]-=1
                l+=1
                
        return count
