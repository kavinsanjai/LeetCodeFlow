class Solution(object):
    def characterReplacement(self, s, k):
        fre_ele={}
        fre_ele[s[0]]=1
        l=0
        most_len=1
        for i in range(1,len(s)):
            fre_ele[s[i]]=fre_ele.get(s[i],0)+1
            most=max(fre_ele.values())
            while((i-l+1)-most>k):
                fre_ele[s[l]]-=1
                l+=1
            most_len=max(i-l+1,most_len)
        return most_len
            




        
        