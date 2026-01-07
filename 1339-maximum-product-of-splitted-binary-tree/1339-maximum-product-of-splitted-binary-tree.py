# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxProduct(self,root): 
        self.sub=[]
        max_sum=0
        def dfs(node):
            if node is None:
                return 0
            sub_sum=node.val + dfs(node.left) + dfs(node.right)
            self.sub.append(sub_sum)
            return sub_sum
        
        total=dfs(root)
        for i in self.sub:
            max_sum=max(max_sum,(total-i)*i)
        
        MOD = 10**9 + 7
        return max_sum % MOD

        
        # queue=deque([root])
        # def findtotal(queue,total_sum):
        #     while queue:
        #         value=queue.popleft()
        #         if value is None:
        #             continue
        #         total_sum+=value.val
        #         queue.append(value.left)
        #         queue.append(value.right)
        #     return total_sum
        
        # total_sum=findtotal(queue,0)
        # def subtree(queue,max_total):
        #     while queue:
        #         value=queue.popleft()
        #         if value is None :
        #             continue
        #         curr=findtotal(deque([value]), 0)
        #         max_total=max(max_total,(total_sum-curr)*curr)
        #         queue.append(value.left)
        #         queue.append(value.right)
        #     return max_total

        # MOD = 10**9 + 7
        # result=subtree(deque([root]), 0)
        # return result % MOD





        # def dfs(node):
        #     if node is None :
        #         return 0
            
        #     left=node.left
        #     right=node.right
        #     total=node.val+left+right
        #     max_value=max(max_val,(total_sum-total)*total)
        #     return max_value
    

        
        