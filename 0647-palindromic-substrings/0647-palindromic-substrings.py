class Solution(object):
    def countSubstrings(self, s):
        count=0
        for i in range(0,len(s)):
            for j in range(i+1,len(s)+1):
                if s[i:j]==s[i:j][::-1]:
                    count+=1
        return count