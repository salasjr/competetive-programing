# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head): 
        stack = []
        values = []
        while head:
            while stack and head.val > values[stack[-1]]:
                values[stack.pop()] = head.val
            stack.append(len(values))
            values.append(head.val)
            head = head.next
        while stack:
            values[stack.pop()] = 0
        return values

 
        