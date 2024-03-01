# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sorted_list=None

        while head:
            nextnode=head.next
            head.next=None

            if sorted_list is None or head.val<=sorted_list.val:
                head.next=sorted_list
                sorted_list=head

            else:
                curr=sorted_list
                while curr.next and curr.next.val <head.val:
                    curr=curr.next
                head.next=curr.next
                curr.next=head

            head=nextnode
        return sorted_list
       
        

        