# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        right,left = ListNode(),ListNode()
        rend,lend = right,left
        while head:
            if head.val < x:
                lend.next = head
                lend = lend.next
            else:
                rend.next = head
                rend = rend.next
            head = head.next
        lend.next = right.next
        rend.next =None
        return left.next
        