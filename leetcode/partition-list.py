# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        first,second=ListNode(),ListNode()
        left,right=first,second
        while head:
            if head.val<x:
                left.next=head
                left=left.next
            else:
                right.next=head
                right=right.next
            head=head.next
        left.next=second.next
        right.next=None
        return first.next

