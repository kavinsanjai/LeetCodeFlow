# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if not root:
            return root
        q=deque([root])
        while q:
            valu=q.popleft()
            if valu.left:
                q.append(valu.left)
            if valu.right:
                q.append(valu.right)
            valu.left,valu.right=valu.right,valu.left
            
        return root