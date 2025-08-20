class Solution(object):
    def wordPattern(self, pattern, s):
        sentence=s.split()
        if len(sentence)!=len(pattern):
            return False
        new={}
        new1={}
        for i , j in zip(pattern,sentence):
            if i in new and new[i]!=j:
                return False                    
            if j in new1 and new1[j]!=i:
                return False
            new[i]=j
            new1[j]=i
        return True