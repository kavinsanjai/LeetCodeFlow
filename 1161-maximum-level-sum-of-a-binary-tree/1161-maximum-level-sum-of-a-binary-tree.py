# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object): 
    def maxLevelSum(self, root):
        if not root:
            return 0
        count=0
        max_count=1
        max_tot=float('-inf')
        queue=deque([root])
        while queue:
            count+=1
            tot=0
            for _ in range(0,len(queue)):
                value=queue.popleft()
                tot+=value.val
                if value.left:
                    queue.append(value.left)
                if value.right:
                    queue.append(value.right)
            if tot>max_tot:
                max_tot=tot
                max_count=count
        return max_count