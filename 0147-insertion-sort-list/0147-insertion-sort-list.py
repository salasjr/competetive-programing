# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sortedList = None

        while head:
            nextNode = head.next
            head.next = None

            if sortedList is None or head.val <= sortedList.val:
                head.next = sortedList
                sortedList = head
            else:
                current = sortedList
                while current.next and current.next.val < head.val:
                    current = current.next
                head.next = current.next
                current.next = head

            head = nextNode
        

        return sortedList





        