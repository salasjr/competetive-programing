# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        prev=dummy
        curr=head
        for i in range(left-1):
            prev=prev.next
            curr=curr.next
        start=curr
        pointer=prev
        for j in range(right-left+1):
            nextt=curr.next
            curr.next=prev
            prev=curr
            curr=nextt
        pointer.next=prev
        start.next=curr
        return dummy.next


        
    

        