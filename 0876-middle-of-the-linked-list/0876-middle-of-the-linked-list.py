# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        fast_temp = head
        slow_temp = head
        
        while fast_temp and fast_temp.next:
            fast_temp = fast_temp.next.next
            slow_temp = slow_temp.next
            
        return slow_temp
        