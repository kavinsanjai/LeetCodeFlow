class Solution(object):
    def maxVowels(self, s, k):
        count=0
        opr={'a','e','i','o','u'}
        new_Var=s[len(s)-k:len(s)]
        for i in range(0,len(new_Var)):
            if new_Var[i] in opr:
                count+=1
        max_count=count
        for i in range(len(s)-k-1,-1,-1):
            if s[i+k] in opr:
                count-=1
            if s[i] in opr:
                count+=1
            max_count=max(max_count,count)
        return max_count
            

        