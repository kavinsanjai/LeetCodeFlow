class Solution(object):
    def longestPalindrome(self, s):
        # org = ''
        # substring=''
        # len1=0
        # for i in range(0,len(s)):
        #     for j in range(i,len(s)+1):
        #         org= s[i:j] 
        #         if (org == org[::-1])and(len(org)>len1):
        #             len1=len(org)
        #             substring = s[i:j] 
        # return substring
        al,ar=0,0
        maxi=0
        for i in range(0,len(s)):
            l=r=i
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if r-l > maxi:
                    maxi=r-l
                    ar,al=r,l
                l-=1
                r+=1
            
            l=i
            r=i+1
            while(l>=0 and r<len(s) and s[l]==s[r]):
                if r-l > maxi:
                    maxi=r-l
                    ar,al=r,l
                l-=1
                r+=1
        return s[al:ar+1]
