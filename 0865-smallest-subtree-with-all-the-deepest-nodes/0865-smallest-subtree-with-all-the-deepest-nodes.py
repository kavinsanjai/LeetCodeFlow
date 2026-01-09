# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
            def dfs(root):
                if not root:
                    return 0,None
                left,lnode=dfs(root.left)
                right,rnode=dfs(root.right)
                if left>right:                                
                    return left+1,lnode
                elif right>left:
                    return right+1,rnode
                else:
                    return left+1,root
            depth,node=dfs(root)
            return node