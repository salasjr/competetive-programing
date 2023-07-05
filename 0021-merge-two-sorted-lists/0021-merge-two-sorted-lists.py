# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        a=ListNode(-1)
        pointer1 = list1
        pointer2 = list2
        
        tail = a
        
        while pointer1 and pointer2:
            if pointer1.val < pointer2.val:
                tail.next = pointer1
                pointer1 = pointer1.next
            else:
                tail.next = pointer2
                pointer2=pointer2.next
            tail = tail.next
            
        while pointer1:
            tail.next = pointer1
            pointer1 = pointer1.next
            tail = tail.next
            
        while pointer2:
            tail.next = pointer2
            tail = tail.next
            pointer2=pointer2.next
        return a.next
        