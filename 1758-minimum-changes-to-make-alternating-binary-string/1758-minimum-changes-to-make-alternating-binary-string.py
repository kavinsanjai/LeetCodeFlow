class Solution(object):
    def minOperations(self, s):
        count_0=('01'*len(s))[:len(s)]
        count_1=('10'*len(s))[:len(s)]
        s_count,f_count=0,0
        for i in range(0,len(s)):
            if s[i]!=count_0[i]:
                f_count+=1
            if s[i]!=count_1[i]:
                s_count+=1
        return min(f_count,s_count)


        