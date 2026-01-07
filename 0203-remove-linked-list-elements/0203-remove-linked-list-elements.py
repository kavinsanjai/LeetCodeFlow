# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        res=ListNode(0,head)
        cur=res
        while cur:
            while cur.next and cur.next.val==val:
                cur.next=cur.next.next
            cur=cur.next
        return res.next