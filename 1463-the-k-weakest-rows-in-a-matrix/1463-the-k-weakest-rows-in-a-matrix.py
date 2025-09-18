class Solution(object):
    def kWeakestRows(self, mat, k):
        new=[]
        result=[]
        for i in range(0,len(mat)):
            count_1=mat[i].count(1)
            new.append((count_1,i))
        new.sort(key=lambda x:(x[0],x[1]))
        for pair in new[:k]:
            result.append(pair[1])   
        return result