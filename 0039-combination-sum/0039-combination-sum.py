class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        def backtrack(arr,currsum,start):
            if currsum>target:
                return
            if currsum==target:
                result.append(list(arr))
                return
            
            for i in range(start,len(candidates)):
                arr.append(candidates[i])
                print(i)
                backtrack(arr,currsum+candidates[i],i)
            
                arr.pop()
        backtrack([],0,0)
        return result



            

                           
