# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        def dfs(node,cur_sum):
            if not node:
                return False
            cur_sum-=node.val
            if not node.left and not node.right and cur_sum==0:
                return True
            return dfs(node.left,cur_sum) or dfs(node.right,cur_sum)
        return dfs(root,targetSum)
        