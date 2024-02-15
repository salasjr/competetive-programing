# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr=head
        check=curr
        curr2=head.next
        checker2=curr2
        while curr and curr.next:
            odd=curr.next
            curr.next=odd.next
            curr=odd  
        while curr2 and curr2.next:
            even=curr2.next
            curr2=even.next
            curr2=even
        dummy=check
        while check.next:
            check=check.next
        check.next=checker2
        return (dummy)
        
       

        