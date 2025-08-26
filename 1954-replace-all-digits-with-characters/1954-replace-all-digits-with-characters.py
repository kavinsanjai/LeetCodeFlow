class Solution(object):
    def replaceDigits(self, s):
        s=list(s)
        for i in range(1,len(s),2):
            num=int(s[i])
            s[i]=chr(ord(s[i-1])+num)
        return ''.join(s)
        
        