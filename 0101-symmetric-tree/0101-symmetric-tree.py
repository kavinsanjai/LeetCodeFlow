# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        q=deque()
        q.append((root.left,root.right))
        while q:
            left,right=q.popleft()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val!=right.val:
                return False
            q.append((left.left,right.right))
            q.append((left.right,right.left))
        return True


        
        