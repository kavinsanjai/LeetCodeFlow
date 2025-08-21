class Solution(object):
    def restoreString(self, s, indices):
        result=[""]*(len(indices)+1)
        for i , j in zip(s,indices):
            result[j]=i
        return ''.join(result)
           
            