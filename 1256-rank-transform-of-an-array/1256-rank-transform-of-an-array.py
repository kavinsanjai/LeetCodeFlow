class Solution(object):
    def arrayRankTransform(self, arr):
        new=sorted(set(arr))
        rank_map={}
        for index,value in enumerate(new):
            rank_map[value]=index+1
        result=[]
        for value in arr:
            result.append(rank_map[value])
        return result