# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2): 
        if not root1:
            return root2
        q=deque([(root1,root2)])
        while q:
            v1,v2=q.popleft()
            if not v2:
                continue
            v1.val+=v2.val
            if not v1.left:
                v1.left=v2.left
            else:
                q.append((v1.left,v2.left))
            
            if not v1.right:
                v1.right=v2.right
            else:
                q.append((v1.right,v2.right))
        return root1
                
    


        