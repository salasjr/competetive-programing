# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        for _ in range(left - 1):
            prev = prev.next
            curr = curr.next
        start = curr
        tail = curr
        con = prev
        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        con.next = prev
        start.next = curr
        return dummy.next
    

        
        