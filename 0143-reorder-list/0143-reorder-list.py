# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        curr=head
        new=[]
        count=0
        while (curr!=None):
            new.append(curr)
            curr=curr.next
            count+=1
        curr=head
        for i in range(0,count//2):
            rev=new.pop()
            rev.next=curr.next
            curr.next=rev
            curr=curr.next.next
        
        curr.next=None
        return head