# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        stack=[]
        while head:
            stack.append(head.val)
            head=head.next 
        stack1=[]
        for i in range(len(stack)-1,-1,-1):
            stack1.append(stack[i])
        return stack ==stack1     
      
        