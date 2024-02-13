# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        head1 = head
        while head1:
            while head1.next and head1.next.val==head1.val:
                head1.next = head1.next.next
            head1 = head1.next
        return head
  
       
        
     