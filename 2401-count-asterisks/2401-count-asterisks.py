class Solution(object):
    def countAsterisks(self, s):
        found=False
        s=list(s)
        for i in range(0,len(s)):
            if found==True and s[i]!='|':
                s[i]=''
            elif s[i]=='|':
                if found==True:
                    found=False
                else:
                    found=True
        return s.count('*')
        